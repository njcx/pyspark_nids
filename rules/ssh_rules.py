# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


ssh = [
    {
            "state": "enable",
            "rule_id": "sqli_get_01",
            "rule_tag": "sqli",
            "rule_name": "sqli_get_select",
            "detect_rule_type": "or",
            "white_list_type": "and",

            "white_list": [

            ],

            "detect_list": [

              # {
              #     "field" : "ssh|client",
              #     "type": "in",
              #     "rule": "SSH"
              # },

              # {
                #               #     "field" : "ssh.id.orig_h",
                #               #     "type": "equal",
                #               #     "rule":"172.19.29.44"
                #               # },

              # {
              #     "field": "ssh|client",
              #     "type": "re",
              #     "rule": "SSH",
              #     "ignorecase": "False"
              # },

                {
                    "field": "ssh|client",
                    "type": "custom_func",
                    "rule": "ssh_nmap_scan",
                }

            ],
            "threat_level": "high",
            "auth": "njcx",
            "info": "about sql injection attack",
            "e-mail": ["xxx", "xxx"]

      }

]