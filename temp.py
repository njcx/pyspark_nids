# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from settings import kafkaParams, SSHGroupId, SSHTopic, CheckPointDir
from utils import json_to_py
from utils import  KafkaTools

def send_partition(iter):
    kafka_utils =KafkaTools(kafkaParams["metadata.broker.list"])
    for record in iter:
        kafka_utils.produce(topic_name,
        connection.send(record)
    # return to the pool for future reuse
    ConnectionPool.returnConnection(connection)



def






# def json_ds():

def create_context():
    sc_conf = SparkConf()
    sc_conf.setAppName('sec-' + SSHTopic)
    sc = SparkContext(conf=sc_conf)
    ssc = StreamingContext(sc, 5)
    msg_stream = KafkaUtils.createDirectStream(ssc, [SSHTopic],
                                               kafkaParams=dict(kafkaParams, **{"group.id": SSHGroupId}))
    msg_stream.checkpoint(20)
    result = msg_stream.map(lambda x: json_to_py(x[1]))

    result.foreachRDD(lambda rdd: rdd.foreachPartition(sendPartition))

    result.pprint()
    ssc.checkpoint(CheckPointDir)
    return ssc


ssc = StreamingContext.getOrCreate(CheckPointDir, create_context)
ssc.start()
ssc.awaitTermination()