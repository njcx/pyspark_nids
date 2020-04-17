redis = [
    {
            "state": "enable",
            "rule_id": "redis_01",
            "rule_tag": "redis",
            "rule_name": "redis_auth",
            "rule_type": "and",

            "detect_list": [

              {
                  "field": "method",
                  "type":  "in",
                  "rule": "AUTH"
              }


            ],
            "threat_level":"high",
            "auth":"njcx",
            "info": "about sql injection attack",
            "e-mail": ["xxx","xxx"]

      }
  ]
