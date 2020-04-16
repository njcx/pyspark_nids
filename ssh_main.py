# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from settings import KafkaParams, SSHGroupId, SSHTopic, CheckPointDir, NidsAlertTopic, SparkLogLevel
from utils import json_to_py, KafkaTools, Engine


def send_partition(iter):

    kafka_utils =KafkaTools(KafkaParams["metadata.broker.list"])
    ssh_check = Engine(rule_type='SSH')

    for record in iter:
        if ssh_check.check_line(record) and ssh_check.check_line(record)[0]:
            kafka_utils.produce(NidsAlertTopic, dict(record,
            **{"rule": {key:ssh_check.check_line(record)[1][key] for key in ssh_check.check_line(record)[1]
                        if key not in ['rule_type', 'detect_list']}}))


def create_context():
    sc_conf = SparkConf()
    sc_conf.setAppName('sec-' + SSHTopic)
    sc = SparkContext(conf=sc_conf)
    sc.setLogLevel(SparkLogLevel)

    ssc = StreamingContext(sc, 5)
    msg_stream = KafkaUtils.createDirectStream(ssc, [SSHTopic],
                                               kafkaParams=dict(KafkaParams, **{"group.id": SSHGroupId}))
    msg_stream.checkpoint(20)
    result = msg_stream.map(lambda x: json_to_py(x[1]))
    result.foreachRDD(lambda rdd: rdd.foreachPartition(send_partition))
    ssc.checkpoint(CheckPointDir)
    return ssc


ssc = StreamingContext.getOrCreate(CheckPointDir, create_context)
ssc.start()
ssc.awaitTermination()