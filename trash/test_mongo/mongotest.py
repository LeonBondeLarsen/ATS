#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from pymongo import MongoClient
import datetime,os

client = MongoClient('localhost', 27017)
db = client['test-database']

post = {"author": "Leon","text": "Sometext","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}

sha_command = "echo \"" + str(post) + "\" | sha1sum | cut -d' ' -f1"
post["_id"] = os.popen(sha_command).read().rstrip()

print post["_id"]

posts = db.posts
post_id = posts.insert_one(post).inserted_id

print post_id
