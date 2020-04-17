# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from pyspark.streaming.kafka import TopicAndPartition
from settings import RedisPasswd, RedisHost
from utils import RedisTool


g_offset_ranges = []
redis_utils = RedisTool(RedisPasswd, RedisHost)


def get_offset_ranges(topic):
    ranges = None
    key = '{topic}:offsets'.format(topic=topic)
    if redis_utils.exists(key):
        mapping = redis_utils.hgetall(key)
        ranges = dict()
        for k, v in mapping.items():
            tp = TopicAndPartition(topic, int(k))
            ranges[tp] = long(v)
    return ranges


def update_offset_ranges(rdd):
    for o in g_offset_ranges:
        key = '{topic}:offsets'.format(topic=o.topic)
        redis_utils.hset(key, o.partition, o.untilOffset)


def store_offset_ranges(rdd):
    global g_offset_ranges
    g_offset_ranges = rdd.offsetRanges()
    return rdd