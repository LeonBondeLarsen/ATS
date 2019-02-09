#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys,json 

while 1:
    try:
        line = sys.stdin.readline()
        event = json.loads(line)
    except KeyboardInterrupt:
        break

    print 'cage: ' + str(event['event']['cage']) + 'ts: ' + event['timestamp'] + '  : ' + event['event']['position'] + ' ' + str(event['duration'])

