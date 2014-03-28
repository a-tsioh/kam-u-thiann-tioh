import json

from elasticsearch import Elasticsearch

datafile = "Data/parsed_keywords_lsa.json"

data = json.load(open(datafile))

es = Elasticsearch()

for i, doc in enumerate(data):
    doc["lsa"]["neighbors"] = [[float(a), float(b)]
                               for a, b in doc["lsa"]["neighbors"]]
    res = es.index(index="fumao", doc_type='irc', id=i, body=doc)

    print i, res

es.indices.refresh(index="fumao")
