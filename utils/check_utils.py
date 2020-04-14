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

    def __init__(self, rule):

        self.rule_ = rule

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

    def check_res(self, data):
        match_conut = 0
        try:

            for detect_item in self.rule_['detect_list']:
                if detect_item['type'] == 'in':
                    if self.check_in(self.res_parser(data, detect_item['field']), detect_item['rule']):
                        match_conut = match_conut +1

                if detect_item['type'] == 're' and detect_item['ignorecase'] == "False":
                    if self.check_re(self.res_parser(data, detect_item['field']), detect_item['rule']):
                        match_conut = match_conut + 1

                if detect_item['type'] == 're' and detect_item['ignorecase'] == "True":
                    if self.check_re(self.res_parser(data, detect_item['field']), detect_item['rule'], I=True):
                        match_conut = match_conut + 1

                if detect_item['type'] == 'equal':
                    if self.check_equal(self.res_parser(data, detect_item['field']), detect_item['rule']):
                        match_conut = match_conut + 1

            if self.rule_['rule_type'] == "and":
                return match_conut == len(self.rule_['detect_list']), self.rule_

            if self.rule_['rule_type'] == "or":
                return bool(match_conut), self.rule_

        except Exception as e:
            logger.error(str(e))
            return False
















