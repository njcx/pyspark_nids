# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


RedisHost = '172.21.129.2'
RedisPort = 6379
RedisPasswd = 'MAAp6aU6bG'


ArangoHost = '172.21.129.2'
ArangoPort = 8529
ArangoUser = "root"
ArangoPasswd = 'MAAp6aU6bG'


MySQLGroupId = "nids-mysql"
MySQLTopic = "nids-mysql"

ConnGroupId = "nids-conn"
ConnTopic = "nids-conn"

HTTPGroupId = "nids-http"
HTTPTopic = "nids-http"

SSHGroupId = "nids-ssh"
SSHTopic = "nids-ssh"

DNSGroupId = "nids-dns"
DNSTopic = "nids-dns"

ICMPGroupId = "nids-icmp"
ICMPTopic = "nids-icmp"

RedisGroupId = "nids-redis"
RedisTopic = "nids-redis"

Log_Path = '/tmp/'

CheckPointDir = "/tmp/spark_check_point"

NidsAlertTopic = "nids_alert"

KafkaParams = {"metadata.broker.list": "172.21.129.2:9092"}


