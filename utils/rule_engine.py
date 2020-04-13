# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from utils.json_ import json_file_to_py
from utils.log_ import Logger
from settings import NidsHome
logger = Logger.get_logger(__name__)


class Engine(object):
    def __init__(self, rule_type):
        self.rule_type = rule_type
        self.rules = self.read_rules()

    def read_rules(self):
        try:
            return json_file_to_py("{0}/rules/{1}.json".format(NidsHome, self.rule_type.lower()))
        except Exception as e:
            logger.error(str(e))
            return {}


if __name__ == '__main__':
    test= Engine(rule_type='HTTP')



