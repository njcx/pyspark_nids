# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


from utils.log_ import Logger

try:
    import re2 as re
except ImportError:
    import re

logger = Logger.get_logger(__name__)


class CheckUtil(object):

    def __init__(self):

        pass

    def res_parser(self, res, field):

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

    def check_in(self, res, pattern):
        try:
            return str(pattern) in str(res).strip()

        except Exception as e:
            logger.error(str(e))
            return False

    def check_equal(self, res, pattern):
        try:
            return str(pattern) == str(res).strip()
        except Exception as e:
            logger.error(str(e))
            return False

    def check_re(self, res, pattern, I=False):

        try:
            if I:
                re_utils = re.compile(pattern, re.I)
                return re_utils.search(str(res).strip())
            else:

                re_utils = re.compile(pattern)
                return re_utils.search(str(res).strip())
        except Exception as e:
            logger.error(str(e))
            return False





