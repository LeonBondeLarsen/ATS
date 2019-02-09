#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from datetime import datetime

d1 = datetime.strptime("09:16:28.044", "%H:%M:%S.%f")
d2 = datetime.strptime("09:16:41.903", "%H:%M:%S.%f")

print "%.3f" % str(d2 - d1)
