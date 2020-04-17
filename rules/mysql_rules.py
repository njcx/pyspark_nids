mysql = [
    {
            "state": "enable",
            "rule_id": "mysql_get_01",
            "rule_tag": "mysql",
            "rule_name": "mysql",
            "rule_type": "and",

            "detect_list": [

              {
                  "field" : "method",
                  "type": "in",
                  "rule": "DROP"
              }


            ],
            "threat_level":"high",
            "auth":"njcx",
            "info": "about sql injection attack",
            "e-mail": ["xxx","xxx"]

      }

  ]