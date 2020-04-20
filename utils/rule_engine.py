# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from utils.check_utils import CheckUtil
from utils.log_ import Logger
logger = Logger.get_logger(__name__)


class Engine(object):
    def __init__(self, rule_type):
        self.rule_type = rule_type
        self.rules_func_list = self.rules_to_func_list()

    def read_rules(self):
        try:
            rules = __import__('rules')
            return getattr(rules, self.rule_type.lower())
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
        return temp_list

    def check_line(self, data):
        temp = []
        try:
            for rule_func in self.rules_func_list:
                temp.append(rule_func.check_res(data))
            return temp
        except Exception as e:
            logger.error(str(e))
        return temp


if __name__ == '__main__':
    test = Engine(rule_type='SSH')

    data = {
    "@timestamp": "2020-04-16T09:01:14.518Z",
    "@version": "1",
    "ssh": {
      "auth_attempts": 1,
      "uid": "CwUwXG2KseeiluBcyk",
      "kex_alg": "diffie-hellman-group-exchange-sha256",
      "host_key": "25:01:d0:55:76:bc:4c:87:96:62:1f:01:7b:29:d8:bd",
      "mac_alg": "hmac-sha1",
      "id.resp_h": "10.10.116.222",
      "cipher_alg": "aes128-cbc",
      "compression_alg": "none",
      "id.orig_h": "172.19.26.59",
      "ts": 1587027674.10733,
      "id.resp_p": 7999,
      "version": 2,
      "id.orig_p": 62346,
      "client": "SSH-2.0-OpenSSH_4.6",
      "host_key_alg": "ssh-rsa",
      "server": "SSH-2.0-OpenSSH_7.4",
      "auth_success": "true"
    }
  }
    print(test.check_line(data))



