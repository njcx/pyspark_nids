# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from settings import KafkaParams, SSHGroupId, SSHTopic , CheckPointDir
from utils import json_to_py


check_point_dir = "/tmp/spark_check_point"


def create_context():
    sc_conf = SparkConf()
    sc_conf.setAppName('sec-' + SSHTopic)
    sc = SparkContext(conf=sc_conf)
    ssc = StreamingContext(sc, 5)
    msg_stream = KafkaUtils.createDirectStream(ssc, [SSHTopic],
                                               kafkaParams=dict(KafkaParams, **{"group.id": SSHGroupId}))
    msg_stream.checkpoint(20)
    result = msg_stream.map(lambda x: json_to_py(x[1]))
    result.pprint()
    ssc.checkpoint(CheckPointDir)
    return ssc


ssc = StreamingContext.getOrCreate(CheckPointDir, create_context)

#
# def out_put(m):
#     print(m)
#
#
# def store_offset(rdd):
#     global offsets
#     offsets = rdd.offsetRanges()
#     return rdd
#
#
# def print_offset(rdd):
#     for o in offsets:
#         print "%s %s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset, o.untilOffset - o.fromOffset)


# KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})

# config = SparkConf()
# sc = SparkContext(appName='sec-' + SSHTopic, )
# ssc = StreamingContext(sc, 2)
# # print kafkaParams.update({"group.id": SSHGroupId})
#
# msg_stream = KafkaUtils.createDirectStream(ssc, [SSHTopic],
#                                            kafkaParams=dict(kafkaParams, **{"group.id": SSHGroupId}))

ssc.start()
ssc.awaitTermination()

