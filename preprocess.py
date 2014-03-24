# -*- coding:utf-8 -*-

import json
import codecs
import sys
import re


datafile = "Data/all.json"

basic_parser = re.compile(u"^(\d+:\d+)? *(\[[^\]]+\])?(?: *([^：:]{0,10})[:：] *)?(.*)$", re.UNICODE)

data = json.load(open(datafile))

for post in data:
    parse = basic_parser.match(post["msg"])
    if not parse:
        print "pb with", post
        sys.exit(1)
    info = parse.groups()
    post["parsed"] = {"date":info[0],"place":info[1], "speaker":info[2], "content":info[3]}

json.dump(data, codecs.open("Data/parsed.json","w","utf8"), ensure_ascii=False, encoding="utf-8")
