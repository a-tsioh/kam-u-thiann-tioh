# -*- coding:utf-8 -*-

import json
import codecs
import sys

keywordsfile = codecs.open("keywords.txt","r","utf8")
datafile = "Data/parsed.json"

keywords = []
for l in keywordsfile:
    l = l.strip()
    keywords.append(l)


data = json.load(open(datafile))
for post in data:
    txt = post["parsed"]["content"]
    post["parsed"]["keywords"] = []
    for w in keywords:
        if w in txt:
            post["parsed"]["keywords"].append(w)

json.dump(data,codecs.open("Data/parsed_keywords.json", "w", "utf8"), ensure_ascii=False, encoding="utf-8")
