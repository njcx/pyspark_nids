# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from settings import KafkaParams, MySQLGroupId, MySQLTopic, NidsAlertTopic, SparkLogLevel
from utils import json_to_py, py_to_json, store_offset_ranges, update_offset_ranges, get_offset_ranges
from utils import Logger, KafkaTools, Engine
logger = Logger.get_logger(__name__)


def send_partition(iter):
    kafka_utils = KafkaTools(KafkaParams["metadata.broker.list"])
    mysql_check = Engine(rule_type='MYSQL')
    for record in iter:
        try:
            if mysql_check.check_line(record):
                for check_result in mysql_check.check_line(record):
                    if check_result[0]:
                        kafka_utils.produce(NidsAlertTopic, py_to_json(dict(record,
                        **{"rule": {key: check_result[1][key] for key in check_result[1]
                                    if key not in ['rule_type', 'detect_list']}})))
        except Exception as e:
            logger.error(str(e))


sc_conf = SparkConf()
sc_conf.setAppName('sec-' + MySQLTopic)
sc = SparkContext(conf=sc_conf)
sc.setLogLevel(SparkLogLevel)
ssc = StreamingContext(sc, 5)
offset_ranges = get_offset_ranges(MySQLTopic)
msg_stream = KafkaUtils.createDirectStream(ssc, [MySQLGroupId],
                                           kafkaParams=dict(KafkaParams, **{"group.id": MySQLGroupId}),
                                           fromOffsets=offset_ranges)
msg_stream.transform(store_offset_ranges).foreachRDD(update_offset_ranges)
result = msg_stream.map(lambda x: json_to_py(x[1]))
result.foreachRDD(lambda rdd: rdd.foreachPartition(send_partition))
ssc.start()
ssc.awaitTermination()