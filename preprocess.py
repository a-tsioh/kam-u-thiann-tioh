# -*- coding:utf-8 -*-

import json
import codecs
import sys
import re


datafile = "Data/all.json"

basic_parser = re.compile(u"^(?: *([^：:]{0,10})[:：] *)?(.*)$", re.UNICODE)

data = json.load(open(datafile))

for post in data:
    parse = basic_parser.match(u" ".join(post["content"]))
    if not parse:
        print "pb with", post
        sys.exit(1)
    info = parse.groups()
    datetime = "2014/%s/%s %s" % (post["month"], post["date"], post["time"])
    post["parsed"] = {"date":datetime,"place":post["location"], "speaker":info[0], "content":info[1]}

json.dump(data, codecs.open("Data/parsed.json","w","utf8"), ensure_ascii=False, encoding="utf-8")
