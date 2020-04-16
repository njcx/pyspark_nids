ssh = [
    {
            "state": "enable",
            "rule_id": "sqli_get_01",
            "rule_tag": "sqli",
            "rule_name": "sqli_get_select",
            "rule_type": "or",

            "detect_list": [

              {
                  "field" : "client",
                  "type": "in",
                  "rule":"Nmap"
              },

              {
                  "field" : "id.orig_h",
                  "type": "equal",
                  "rule":"172.19.29.44"
              },

              {
                  "field" : "client",
                  "type": "re",
                  "rule":"Nmap",
                  "ignorecase": "False"
              }

            ],
            "threat_level":"high",
            "auth":"njcx",
            "info": "about sql injection attack",
            "e-mail": ["xxx","xxx"]

      }

]