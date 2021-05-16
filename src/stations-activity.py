#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:44:22 2021

@author: Saba Kiriako
"""



import json
from kafka import KafkaConsumer, KafkaProducer

stations = {}
consumer = KafkaConsumer("velib-stations", bootstrap_servers='localhost:9092')
host = "9092"
producer = KafkaProducer(bootstrap_servers="localhost:"+str(host))
topic_name="stations-status"

statuses = {}
for message in consumer:
    i=0
    stations = json.loads(message.value.decode())
    for station in stations:
        key = "{}-{}-{}".format(station["number"], station["name"], station["contract_name"])
        status = station["available_bikes"]
        if key not in statuses.keys(): 
            statuses[key] = status
        else:   
            if status != statuses[key] :
                print("Current Status :" + str(status) +" Previous Status :" + str(statuses[key]))
                producer.send(topic_name, json.dumps(station).encode())
                statuses[key] = status
                i+=1
    print("Number of stations where there status changed :" +str(i))
    print("")
                
        
