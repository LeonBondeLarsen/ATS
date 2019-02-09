#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,time,sys,json,copy
from datetime import datetime
from kafka import KafkaProducer

class EventEmitter():
    def __init__(self, servers, topic):
        self.servers = servers
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.servers)
        
        self.event = dict()

    def send(self):
        tmp = copy.deepcopy(self.event)
        tmp["@timestamp"] = self.event["@timestamp"].isoformat()
        payload = json.dumps(tmp)
        print payload
        self.producer.send(self.topic, payload.encode())

    def update_event(self):
        pass

from sense_hat import SenseHat

class TemperatureEventEmitter(EventEmitter):
    def __init__(self, servers, topic, identifier):
        EventEmitter.__init__(self, servers, topic)

        self.contents = dict()
        self.contents["id"] = identifier
        
        self.event["@timestamp"] = datetime.utcnow()
        self.event["data"] = self.contents
        
        self.sense = SenseHat()

    def update_event(self):
        self.event["@timestamp"] = datetime.utcnow()
        self.event["data"]["temperature"] = round(self.sense.get_temperature_from_pressure()-9.0,1)
        self.event["data"]["pressure"] = round(self.sense.get_pressure(),1)
        self.event["data"]["humidity"] = round(self.sense.get_humidity(),1)
        self.send() 

if __name__ == "__main__":

    servers = str( os.environ.get('_kafka_servers') )
    topic = str( os.environ.get('_kafka_topic') )
    identifier = str( os.environ.get('_identifier' ) )
    output_period = float( os.environ.get('_output_period') )

    event_emitter = TemperatureEventEmitter(servers, topic, identifier)

    try:
        while True:
            event_emitter.update_event()
            time.sleep(output_period) 
    except KeyboardInterrupt:
        sys.stdout.flush()
        pass

