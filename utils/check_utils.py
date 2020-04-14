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
        #
        # temp_list = []
        # rules = self.read_rules()
        # for rule in rules:
        #     rule['func_list'] = []
            for detect_item in self.rule_['detect_list']:

            if self.rule_['type'] == 'in':
                rule['func_list'].append(check_in(res_parser(detect_item['field']), detect_item['field']))

            if self.rule_['type'] == 're':
                rule['func_list'].append(check_re(res_parser(detect_item['field'])))

            if self.rule_['type'] == 're':
                rule['func_list'].append(check_re(res_parser(detect_item['field'])))












