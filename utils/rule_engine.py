# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from utils.json_ import json_file_to_py
from utils.check_utils import CheckUtil
from utils.log_ import Logger
from settings import NidsHome
logger = Logger.get_logger(__name__)


class Engine(object):
    def __init__(self, rule_type):
        self.rule_type = rule_type
        self.rules_func_list = self.rules_to_func_list()

        print self.rules_func_list

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
                temp_list.append(CheckUtil(rule))

            return temp_list

        except Exception as e:
            logger.error(str(e))
            return {}

    def check_line(self, data):

        for rule_func in self.rules_func_list:

            print rule_func.check_res(data)


if __name__ == '__main__':
    test = Engine(rule_type='SSH')

    data = {
      "ts": 1586852099.89234,
      "id.resp_h": "10.10.252.121",
      "uid": "CtJwAA2XWyrbnfKztd",
      "id.resp_p": 22,
      "auth_attempts": 0,
      "client": "SSH-2.0-Nmap-SSH2-Hostkey",
      "id.orig_p": 56871,
      "cipher_alg": "aes128-cbc",
      "compression_alg": "none",
      "mac_alg": "hmac-sha1",
      "kex_alg": "diffie-hellman-group1-sha1",
      "server": "SSH-2.0-OpenSSH_7.4",
      "id.orig_h": "172.19.29.44",
      "version": 2,
      "host_key_alg": "Algorithm negotiation failed"
    }

    print test.check_line(data)



