#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Test:
# {(while true;do;echo "{\"timestamp\":\"$(date +%T.%3N)\",\"front\":0,\"back\":0}";sleep 0.1;done)&;(while true;do;echo "{\"timestamp\":\"$(date +%T.%3N)\",\"front\":0,\"back\":0}";sleep 0.1;done)} | python position_monitor.py

import json
import sys

while 1:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        break

    data = json.loads(line)
    print data['timestamp']



