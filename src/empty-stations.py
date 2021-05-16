#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:23:30 2021

@author: Saba Kiriako
"""

import json
from kafka import KafkaConsumer, KafkaProducer

stations = {}
consumer = KafkaConsumer("stations-status", bootstrap_servers='localhost:9092')
consumer2 = KafkaConsumer("velib-stations", bootstrap_servers='localhost:9092')
host = "9092"
producer = KafkaProducer(bootstrap_servers="localhost:"+str(host))
topic_name="empty-stations"

available_bikes = {}

"""Here I am initializing all the stations status before starting."""
for message in consumer2:
    stations = json.loads(message.value.decode())
    for station in stations:
        key = "{}-{}-{}".format(station["number"], station["name"], station["contract_name"])
        bikes = station["available_bikes"]
        available_bikes[key] = bikes
    break

print("Finish Initialization")

for message in consumer:
    station = json.loads(message.value.decode())
    key = "{}-{}-{}".format(station["number"], station["name"], station["contract_name"])
    bikes = station["available_bikes"]
    if key not in available_bikes.keys(): 
        available_bikes[key] = bikes
    else:   
        if (available_bikes[key]==0 and bikes > 0) or (available_bikes[key] > 0 and bikes ==0):
            print(station['name'])
            print("Current available bikes Number :" + str(bikes) +" Previous available bikes Number :" + str(available_bikes[key]))
            print("")
            producer.send(topic_name, json.dumps(station).encode())
        available_bikes[key] = bikes
        
