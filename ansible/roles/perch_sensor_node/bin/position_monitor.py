#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,time,sys,json,copy
from datetime import datetime

# Service settings
front_gpio_path = str(sys.argv[1])
back_gpio_path = str(sys.argv[2])
sensor_poll_period = float(sys.argv[3])
bird = int(sys.argv[4])

# Internal data structures
position = 'INIT'
previous_position = 'INIT'

current_event = dict()
previous_event = dict()
contents = dict()
first_run_done = False

front_state = 1
back_state = 1

running_average_size = 10
latest_front = [1]*running_average_size
latest_back = [1]*running_average_size
sample_pointer = 0

def init_events():
    contents["id"] = bird
    contents["position"] = position
    contents["duration"] = 0.0
    
    current_event["@timestamp"] = datetime.utcnow()
    current_event["data"] = contents

    previous_event = copy.deepcopy(current_event)

def get_gpio_value( gpio_path ):
    gpio_handle = open(gpio_path, 'r')
    gpio_state = gpio_handle.read().rstrip()
    gpio_handle.close()
    return gpio_state

def get_position( front_state, back_state):
    position = 'ERROR'
    if front_state == '0':
        if back_state == '0':
            position = 'ERROR'
        else:
            position = 'FRONT'
    else:
        if back_state == '0':
            position = 'BACK'
        else:
            position = 'BOTTOM'
    return position

def get_time_since_last_event():
    current_time = current_event["@timestamp"]
    previous_time = previous_event["@timestamp"]
    return (current_time - previous_time).total_seconds()


def convert_to_iso(datetime_in):
        tmp = copy.deepcopy(datetime_in)
        tmp['@timestamp'] = datetime_in['@timestamp'].isoformat()
        return tmp


init_events()
while True:
    try:
        front_state = get_gpio_value(front_gpio_path)
        back_state = get_gpio_value(back_gpio_path)
        position = get_position(front_state,back_state)

        if position != previous_position:

            # Update current event
            current_event["@timestamp"] = datetime.utcnow()
            current_event["data"]["position"] = position
            current_event["data"]["duration"] = 0.0

            if first_run_done:
                # Send current event
                output_event = convert_to_iso(current_event)
                print json.dumps(output_event)
                sys.stdout.flush()

                # Calculate duration of previous event
                previous_event["data"]["duration"] = get_time_since_last_event()

                # Send previous event
                output_event = convert_to_iso(previous_event)
                print json.dumps(output_event)
                sys.stdout.flush()
            else:
                first_run_done = True

            # Upkeep
            previous_event = copy.deepcopy(current_event)
            previous_position = position;


        time.sleep (sensor_poll_period);
    except KeyboardInterrupt:
        break

