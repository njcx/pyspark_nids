# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


from utils.log_ import Logger

try:
    import re2 as re
except ImportError:
    import re

logger = Logger.get_logger(__name__)


def check_in((res, pattern)):

    try:
        return pattern in res

    except Exception as e:
        logger.error(str(e))
        return False


def check_equal(res, pattern):
    try:
        return pattern == res
    except Exception as e:
        logger.error(str(e))
        return False


def check_re((res, pattern)):

    pass


def res_parser(res, field):

    try:
        if field in res:
            return str(res[field]).strip()

        else:
            temp_ = field.split('.')
            for _ in temp_:
                res = res[_]
        return str(res).strip()

    except Exception as e:
        logger.error(str(e))


