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
    sc_conf.set('spark.executor.memory', '2g')
    sc_conf.set("spark.executor.cores", 4)
    sc_conf.set('spark.cores.max', 4)  # spark.cores.max：为一个application分配的最大cpu核心数，如果没有设置这个值默认为spark.deploy.defaultCores
    # sc_conf.set('spark.logConf', True)  # 当SparkContext启动时，将有效的SparkConf记录为INFO。

    sc = SparkContext(conf=sc_conf)

    # sc = SparkContext(appName='sec-' + SSHTopic, )
    ssc = StreamingContext(sc, 1)

    # lines = ssc.socketTextStream(...)  # create DStreams
    # ...

    msg_stream = KafkaUtils.createDirectStream(ssc, [SSHTopic],
                                               kafkaParams=dict(kafkaParams, **{"group.id": SSHGroupId}))

    msg_stream.checkpoint(10)

    result = msg_stream.map(lambda x: json_to_py(x[1]))
    # msg_stream.transform(store_offset, ).foreachRDD(print_offset)
    result.pprint()

    ssc.checkpoint(checkpointDirectory)  # set checkpoint directory
    return ssc


context = StreamingContext.getOrCreate(checkpointDirectory, create_context)

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

context.start()
context.awaitTermination()