#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 20:19:10 2021

@author: saba
"""


import json
from kafka import KafkaConsumer


consumer = KafkaConsumer("empty-stations", bootstrap_servers='localhost:9092')
host = "9092"

stations_empty = []
for message in consumer:
    station = json.loads(message.value.decode())
    available_bikes = station["available_bikes"]
    key = "{}-{}-{}".format(station["number"], station["name"], station["contract_name"])
    if (available_bikes == 0) and (key not in stations_empty): #this is a way to print only once the station that is empty
        print("Empty Station Alert :")
        print("Address :" + str(station['address']))
        print("City :" + str(station['contract_name']))
        print("")
        stations_empty.append(key)
    elif (available_bikes > 0)  and (key in stations_empty):
        stations_empty.remove(key)
         
            
        