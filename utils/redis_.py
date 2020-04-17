
# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : redis.py

import redis
import datetime
from utils.log_ import Logger
logger = Logger.get_logger(__name__)


class RedisTool(object):

    def __init__(self, password=None, host='127.0.0.1', port=6379, db=0):
        try:

            redis_pool = redis.ConnectionPool(host=host, port=port, db=db, password=password, max_connections=40)
            self.r = redis.Redis(connection_pool=redis_pool, decode_responses=True)

        except Exception as e:
            logger.error(str(e))

    def rpush(self, key, *value):
        try:
            self.r.rpush(key, *value)
        except Exception as e:
            logger.error(str(e))

    def rpushx(self, key, value):
        try:
            self.r.rpushx(key, value)
        except Exception as e:
            logger.error(str(e))

    def brpop(self, key, timeout):
        try:
            return self.r.brpop(key, timeout)
        except Exception as e:
            logger.error(str(e))

    def llen(self, key):
        try:
            return self.r.llen(key)
        except Exception as e:
            logger.error(str(e))

    def lpush(self, key, value):
        try:
            self.r.lpush(key, value)
        except Exception as e:
            logger.error(str(e))

    def lpushx(self, key, value):
        try:
            self.r.lpushx(key, value)
        except Exception as e:
            logger.error(str(e))

    def lindex(self, key, index):
        try:
            return self.r.lindex(key, index)
        except Exception as e:
            logger.error(str(e))

    def lrange(self, key, start, end):
        try:
            return self.r.lrange(key, start, end)
        except Exception as e:
            logger.error(str(e))

    def zcard(self, key):
        try:
            return self.r.zcard(key)
        except Exception as e:
            logger.error(str(e))

    def zadd(self, key, score, value):
        try:
            return self.r.zadd(key, score, value)
        except Exception as e:
            logger.error(str(e))

    def set(self, key, value, ex):
        try:
            return self.r.set(key, value, ex)

        except Exception as e:
            logger.error(str(e))

    def setnx(self, key, value):
        try:
            return self.r.setnx(key, value)
        except Exception as e:
            logger.error(str(e))

    def get(self, key):
        try:
            return self.r.get(key)
        except Exception as e:
            logger.error(str(e))

    def mget(self, keys):

        try:
            return self.r.mget(keys)
        except Exception as e:
            logger.error(str(e))

    def msetnx(self, key, value):

        try:
            return self.r.msetnx(key, value)
        except Exception as e:
            logger.error(str(e))

    def mset(self, key, value):

        try:
            return self.r.mset(key, value)
        except Exception as e:
            logger.error(str(e))

    def hset(self, key, key1, value):
        try:
            return self.r.hset(key, key1, value)
        except Exception as e:
            logger.error(str(e))

    def hdel(self, key, keys):
        try:
            return self.r.hdel(key, keys)
        except Exception as e:
            logger.error(str(e))

    def hget(self, key, key1):
        try:
            return self.r.hget(key, key1)
        except Exception as e:
            logger.error(str(e))

    def hmget(self, key, key1):
        try:
            return self.r.hmget(key, key1)
        except Exception as e:
            logger.error(str(e))

    def hgetall(self, key):
        try:
            return self.r.hgetall(key)
        except Exception as e:
            logger.error(str(e))

    def hmset(self, key, kv):
        try:
            return self.r.hmset(key, kv)
        except Exception as e:
            logger.error(str(e))

    def exists(self, key):
        try:
            return self.r.exists(key)
        except Exception as e:
            logger.error(str(e))

    def del_key(self, key):
        try:
            return self.r.delete(key)
        except Exception as e:
            logger.error(str(e))


if __name__ == '__main__':
    try:
        nowTime = datetime.datetime.now().strftime('%Y/%m/%d')
        test = RedisTool(db=1)
        test.rpush(nowTime, 'test')
        print(test.llen(nowTime))
    except Exception as e:
        logger.error(str(e))


