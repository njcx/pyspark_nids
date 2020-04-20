# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from utils.log_ import Logger
try:
    import re2 as re
except ImportError:
    import re
logger = Logger.get_logger(__name__)


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


def check_in(res, pattern):
    try:
        return str(res).strip() in pattern
    except Exception as e:
        logger.error(str(e))
        return False


def check_equal(res, pattern):
    try:
        return str(pattern) == str(res).strip()
    except Exception as e:
        logger.error(str(e))
        return False


def check_re(res, re_utils):
    try:
        return re_utils.search(str(res).strip())
    except Exception as e:
        logger.error(str(e))
        return False


def check_custom_func(res, custom_func):
    try:
        rules = __import__('rules')
        return getattr(rules, custom_func)(res)
    except Exception as e:
        logger.error(str(e))
        return False


class CheckUtil(object):

    def __init__(self, rule):
        self.rule_ = rule
        for detect_item in self.rule_['detect_list']:
            if detect_item['type'] == 're' and detect_item['ignorecase'] == "True":
                detect_item['rule'] = re.compile(detect_item['rule'], re.I)
            if detect_item['type'] == 're' and detect_item['ignorecase'] == "False":
                detect_item['rule'] = re.compile(detect_item['rule'])

    def check_res(self, data):
        match_conut = 0
        white_item_conut = 0
        try:

            if self.rule_['white_list']:
                for white_item in self.rule_['white_list']:
                    if check_in(res_parser(data, white_item['field']), white_item['rule']):
                        white_item_conut = white_item_conut+1

                if self.rule_['white_list_type'] == "and":
                    if white_item_conut == len(self.rule_['white_list']):
                        return False, None

                if self.rule_['white_list_type'] == "or":
                    if white_item_conut > 0:
                        return False, None

            for detect_item in self.rule_['detect_list']:
                if detect_item['type'] == 'in':
                    if check_in(res_parser(data, detect_item['field']), detect_item['rule']):
                        match_conut = match_conut + 1
                if detect_item['type'] == 're':
                    if check_re(res_parser(data, detect_item['field']), detect_item['rule']):
                        match_conut = match_conut + 1

                if detect_item['type'] == 'equal':
                    if check_equal(res_parser(data, detect_item['field']), detect_item['rule']):
                        match_conut = match_conut + 1

                if detect_item['type'] == 'custom_func':
                    if check_custom_func(res_parser(data, detect_item['field']), detect_item['rule']):
                        match_conut = match_conut + 1

            if self.rule_['rule_type'] == "and":
                return match_conut == len(self.rule_['detect_list']), self.rule_
            if self.rule_['rule_type'] == "or":
                return bool(match_conut), self.rule_
        except Exception as e:
            logger.error(str(e))
            return False
















