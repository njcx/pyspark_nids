redis = [
    {
            "state": "enable",
            "rule_id": "sqli_get_01",
            "rule_tag": "sqli",
            "rule_name": "sqli_get_select",
            "detect_rule_type": "and",
            "white_list_type": "and",

            "white_list": [
                {
                    "field": "network.ip",
                    "type": "re",
                    "rule": "xxx",
                    "ignorecase": "False"

                },

                {
                    "field": "network.ip",
                    "type": "equal",
                    "rule": "xxx"
                },

                {
                    "field": "network.ip",
                    "type": "in",
                    "rule": [],
                }
            ],

            "detect_list": [

              {
                 "field": "network.ip",
                  "type": "re",
                  "rule": "xxx",
                  "ignorecase": "False"

              },

              {
                 "field": "network.ip",
                  "type": "equal",
                  "rule": "xxx"
              },


              {
                  "field":  "network.ip",
                  "type":  "in",
                  "rule": 100
              }


            ],
            "threat_level": "high",
            "auth": "njcx",
            "info": "about sql injection attack",
            "e-mail": ["xxx", "xxx"]

      },


     {
              "state": "enable",
              "rule_id": "sqli_get_01",
              "rule_tag": "sqli",
              "rule_name": "sqli_get_select",
              "rule_type": "or",


              "detect_list": [

                {
                 "field" : "network.ip",
                  "type": "re",
                  "rule":"xxx",
                 "ignorecase": "False"
              },

                {
                 "field" : "network.ip",
                  "type": "equal",
                  "rule":"xxx"
              },


              {
                  "field" : "network.ip",
                  "type": "in",
                  "rule":100
              }


              ],
              "threat_level":"high",
              "auth":"njcx",
              "info": "about sql injection attack",
              "e-mail": ["xxx","xxx"]
        },

     {
              "state": "enable",
              "rule_id":"sqli_get_01",
              "rule_tag":"sqli",
              "rule_name":"sqli_get_select",
              "rule_type":"frequency",

              "detect_list": [
                {
                 "field" : "network.ip",
                  "type": "re",
                  "rule": "xxx",
                  "ignorecase": "False"
              },

                {
                 "field" : "network.ip",
                  "type": "equal",
                  "rule":"xxx"
              },

              {
                  "field" : "network.ip",
                  "type": "in",
                  "rule":100
              }


              ],


              "key" :["", ""],

              "time_interval":{
                "second": 10,
                "times":100
              },

              "threat_level":"high",

              "auth":"njcx",

              "info": "about sql injection attack",
              "e-mail": ["xxx","xxx"]
        }

  ]
