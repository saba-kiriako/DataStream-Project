#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 20:59:07 2021

@author: saba
"""

from kafka import KafkaConsumer, TopicPartition
import time

topics=['velib-stations','stations-status','empty-stations']
consumer = KafkaConsumer("velib-stations", bootstrap_servers='localhost:9092')


while True:
    for topic in topics:
        consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092')
        tp = consumer.partitions_for_topic(topic)
        for i in tp:
            topic_partition = TopicPartition(topic, i)
            offset = consumer.position(topic_partition)
            consumer.seek_to_end()
            print("Topic: {} Partition {} offset: {} timestamp: {}".format(topic, i, offset, time.time()))
            print("")
    time.sleep(10)
