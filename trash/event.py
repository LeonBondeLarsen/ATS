#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import json,os
event = dict()
event["timestamp"] = os.popen('date +%T.%3N').read().rstrip()
event["duration"] = 0

contents = dict()
contents["cage"] = 1
contents["position"] = "BOTTOM"

event["event"] = contents

sha_command = "echo \"" + str(event) + "\" | sha1sum | cut -d' ' -f1"
event["identifier"] = os.popen(sha_command).read().rstrip()

json_string = json.dumps(event)

print json_string

