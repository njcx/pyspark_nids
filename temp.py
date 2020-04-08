# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from settings import kafkaParams, SSHGroupId, SSHTopic
from utils import json_to_py

offsets = []

checkpointDirectory = "/tmp"


def create_context():

    sc_conf = SparkConf()
    sc_conf.setAppName('sec-' + SSHTopic)
    sc = SparkContext(conf=sc_conf)

    # sc = SparkContext(appName='sec-' + SSHTopic, )
    ssc = StreamingContext(sc, 1)


    # ...

    msg_stream = KafkaUtils.createDirectStream(ssc, [SSHTopic],
                                               kafkaParams=dict(kafkaParams, **{"group.id": SSHGroupId}))

    msg_stream.checkpoint(10)

    result = msg_stream.map(lambda x: json_to_py(x[1]))
    # msg_stream.transform(store_offset, ).foreachRDD(print_offset)
    result.pprint()

    ssc.checkpoint(checkpointDirectory)  # set checkpoint directory
    return ssc


ssc = StreamingContext.getOrCreate(checkpointDirectory, create_context)

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