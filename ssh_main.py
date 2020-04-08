# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from pyspark import SparkContext
# from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from settings import kafkaParams, SSHGroupId, SSHTopic
from utils import json_to_py

offsets = []

check_point_dir = "/tmp/spark_check_point"


# def functionToCreateContext():
#
#     ssc.checkpoint(checkpointDirectory)  # set checkpoint directory
#     return ssc
#
#
# context = StreamingContext.getOrCreate(checkpointDirectory, functionToCreateContext)


def out_put(m):
    print(m)


def store_offset(rdd):
    global offsets
    offsets = rdd.offsetRanges()
    return rdd


def print_offset(rdd):
    for o in offsets:
        print "%s %s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset, o.untilOffset - o.fromOffset)


# KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})

# config = SparkConf()
sc = SparkContext(appName='sec-' + SSHTopic, )
ssc = StreamingContext(sc, 2)

ssc.checkpoint(check_point_dir)

# lines = ssc.socketTextStream(...)  # create DStreams
# ...

msg_stream = KafkaUtils.createDirectStream(ssc, [SSHTopic],
                                           kafkaParams=dict(kafkaParams, **{"group.id": SSHGroupId}))

result = msg_stream.map(lambda x: json_to_py(x[1]))
msg_stream.transform(store_offset, ).foreachRDD(print_offset)
result.pprint()




ssc.start()
ssc.awaitTermination()