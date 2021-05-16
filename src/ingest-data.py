#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:17:15 2021

@author: Saba Kiriako
"""
import json
import time
import requests
from kafka import KafkaProducer

API_KEY = "f3996e3784384b01ae4a8444d4b26205ac678e04"
host = "9092"
topic_name="velib-stations"

url = "https://api.jcdecaux.com/vls/v1/stations?apiKey="+str(API_KEY)
producer = KafkaProducer(bootstrap_servers="localhost:"+str(host))

while True:
    response = requests.get(url)
    stations = response.json()
    producer.send(topic_name,json.dumps(stations).encode())
    print("Producer sent : Number of Stations Sent is : " + str(len(stations)))
    time.sleep(10)
