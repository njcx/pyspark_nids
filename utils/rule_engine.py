# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from utils.json_ import json_file_to_py
# from utils.check_utils import check_in, check_re, check_equal, res_parser
from utils.log_ import Logger
from settings import NidsHome
logger = Logger.get_logger(__name__)


class Engine(object):
    def __init__(self, rule_type):
        self.rule_type = rule_type
        self.rules_func_list= self.rules_to_func_list()


    def read_rules(self):
        try:
            return json_file_to_py("{0}/rules/{1}.json".format(NidsHome, self.rule_type.lower()))
        except Exception as e:
            logger.error(str(e))
            return {}




    def rules_to_func_list(self):
        try:
            temp_list = []
            rules = self.read_rules()
            for rule in rules:
                rule['func_list'] = []
                for detect_item in rule['detect_list']:

                    # if detect_item['type'] == 'in':
                    #     rule['func_list'].append(check_in(res_parser(detect_item['field']), detect_item['field']))
                    #
                    # if detect_item['type'] == 're':
                    #     rule['func_list'].append(check_re(res_parser(detect_item['field'])))


                    print detect_item


                    # temp_list.append(rule)


        except Exception as e:
            logger.error(str(e))
            return {}




    def check_line(self):

        pass



if __name__ == '__main__':
    test= Engine(rule_type='HTTP')



