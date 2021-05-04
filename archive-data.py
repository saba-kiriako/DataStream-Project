#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 20:32:24 2021

@author: saba
"""

import json
from kafka import KafkaConsumer, KafkaProducer
stations = {}
consumer = KafkaConsumer("velib-stations", bootstrap_servers='localhost:9092')
host = "9092"

with open('data.txt', 'a+') as outfile:
    for message in consumer:
        stations = json.loads(message.value.decode())
        json.dump(stations, outfile)
        outfile.write('\n')
        