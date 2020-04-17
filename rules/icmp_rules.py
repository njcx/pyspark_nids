icmp = [
    {
            "state": "enable",
            "rule_id": "icmp_01",
            "rule_tag": "icmp",
            "rule_name": "icmp",
            "rule_type": "or",

            "detect_list": [

              {
                  "field" : "icmp.request.message",
                  "type": "in",
                  "rule": "Unreachable"
              }


            ],
            "threat_level":"high",
            "auth":"njcx",
            "info": "about sql injection attack",
            "e-mail": ["xxx","xxx"]

      }
  ]