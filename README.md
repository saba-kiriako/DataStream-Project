# Monitoring Vélib Stations
## DataStream Project

We will use Vélib API, that allows to monitor bike stations in many cities, to observe real-time rentals at each station.
This project was made using Kafka.

![alt text](https://play-lh.googleusercontent.com/hlBBO-dmeIbAriEsyzJMDkJx9gYCsfB-LMSiYSJqTrc57_gpxAk6pDM358TMhkKVkw)

## Features

- Status verification of each station.
- Alert when a station becomes empty, and write the address of the station.
- Save logs.
- Real-time monitoring.

## Description

- ingest-data.py - Queries the Bike Sharing System API in a regular interval of time.
- stations-activity.py - Verifies the status of each station.
- empty-stations.py - send a message to a topic“empty-stations”as soon as a station becomes empty or no longer empty.
- alert-empty-stations.py - Prints amessage in the console as soon as a station becomes empty.
- archive-data.py - Archives the input datainthetopic “velib-stations”in a text file.
- monitor-kafka.py - Monitors all the Kafka topics and printsthe status of each Kafka topic.


# Installation

## Download Kafka

- Scala 2.12 : https://www.apache.org/dyn/closer.cgi?path=/kafka/2.7.0/kafka_2.12-2.7.0.tgz
  - $ tar -xzf kafka_2.13-2.7.0.tgz 
  - $ cd kafka_2.13-2.7.0

## Download Kafka for python

pip install kafka-python

# Configuration

- Execute on terminal 1: $ bin/zookeeper-server-start.shconfig/zookeeper.properties
- Execute on terminal 2: $ bin/kafka-server-start.shconfig/server.properties
- Execute ingest-data.py
- Execute stations-activity.py
- Execute empty-stations.py
- Execute alert-empty-stations.py
- Execute archive-data.py
- Execute monitor-kafka.py




<br><br>


For any error or mistake, please contact me on my email sabakiriako@outlook.com, or on my [Linkedin](https://www.linkedin.com/in/sabakiriako/). I know you wont find any but in case 😉
