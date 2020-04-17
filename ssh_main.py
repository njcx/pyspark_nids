# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from settings import KafkaParams, SSHGroupId, SSHTopic, CheckPointDir, NidsAlertTopic, SparkLogLevel
from utils import json_to_py, py_to_json, KafkaTools, Engine
from utils import Logger
logger = Logger.get_logger(__name__)


def get_offset_ranges(topic):
    ranges = None

    rk = '{topic}:offsets'.format(topic=topic)
    cache = redis.Redis()
    if cache.exists(rk):
        mapping = cache.hgetall(rk)
        ranges = dict()
        for k, v in mapping.items():
            tp = TopicAndPartition(topic, int(k))
            ranges[tp] = long(v)

    return ranges


def update_offset_ranges(offset_ranges):
    cache = redis.Redis()
    for rng in offset_ranges:
        rk = '{rng.topic}:offsets'.format(rng=rng)
        print("updating redis_key: {}, partion:{} , lastOffset: {} ".format(rk, rng.partition, rng.untilOffset))
        cache.hset(rk, rng.partition, rng.untilOffset)


def send_partition(iter):
    kafka_utils = KafkaTools(KafkaParams["metadata.broker.list"])
    ssh_check = Engine(rule_type='SSH')
    for record in iter:
        try:
            if ssh_check.check_line(record):
                for check_result in ssh_check.check_line(record):
                    if check_result[0]:
                        kafka_utils.produce(NidsAlertTopic, py_to_json(dict(record,
                        **{"rule": {key: check_result[1][key] for key in check_result[1]
                                    if key not in ['rule_type', 'detect_list']}})))
        except Exception as e:
            logger.error(str(e))


# def create_context():
sc_conf = SparkConf()
sc_conf.setAppName('sec-' + SSHTopic)
sc = SparkContext(conf=sc_conf)
sc.setLogLevel(SparkLogLevel)

ssc = StreamingContext(sc, 5)
msg_stream = KafkaUtils.createDirectStream(ssc, [SSHTopic],
                                           kafkaParams=dict(KafkaParams, **{"group.id": SSHGroupId}))
# msg_stream.checkpoint(20)
result = msg_stream.map(lambda x: json_to_py(x[1]))
result.foreachRDD(lambda rdd: rdd.foreachPartition(send_partition))
    # ssc.checkpoint(CheckPointDir)
    # return ssc


# ssc = StreamingContext.getOrCreate(CheckPointDir, create_context)
ssc.start()
ssc.awaitTermination()