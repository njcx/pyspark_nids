# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from pyspark import SparkContext
# from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from settings import kafkaParams, ConnGroupId, ConnTopic
from utils import json_to_py

offsets = []


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
scontext = SparkContext(appName="sec-"+ConnTopic, )
stream_context = StreamingContext(scontext, 2)
msg_stream = KafkaUtils.createDirectStream(stream_context, [ConnTopic],
                                           kafkaParams=dict(kafkaParams, **{"group.id": ConnGroupId}))
result = msg_stream.map(lambda x: json_to_py(x[1]))
msg_stream.transform(store_offset, ).foreachRDD(print_offset)
result.pprint()
stream_context.start()
stream_context.awaitTermination()
