# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


from utils.log_ import Logger
from confluent_kafka import Consumer, Producer
logger = Logger.get_logger(__name__)


class KafkaTools(object):

    def __init__(self, BROKER_URL):
        self.BROKER_URL = BROKER_URL

    def produce(self, topic_name, msg):
        p = Producer({"bootstrap.servers": self.BROKER_URL})
        p.produce(topic_name, msg)
        p.flush()

    def consume(self, topic_name, group_id="sec-nids"):
        c = Consumer(
            {"bootstrap.servers": self.BROKER_URL, "group.id": group_id,
             'enable.auto.commit': True,
             'default.topic.config': {'auto.offset.reset': 'latest'}})
        c.subscribe([topic_name])
        return c


if __name__ == "__main__":

    BROKER_URL = "PLAINTEXT://172.21.129.2:9092"
    TOPIC_NAME = "nids-http"

    test = KafkaTools(BROKER_URL=BROKER_URL)
    c = test.consume(topic_name=TOPIC_NAME)

    while True:
        message = c.poll(10)
        if message is None:
            print("no message received by consumer")
        elif message.error() is not None:
            print("error from consumer {0}".format(message.error()))
        else:
            print("consumed message {0} : {1}".format(message.key(), message.value()))
    c.close()
