from django.http import HttpResponse
import elasticsearch
import json

es = elasticsearch.Elasticsearch()


def build_doc(doc_id, index="fumao", threshold=0.9):
    doc = es.get(index=index, id=doc_id)["_source"]
    neighbors = []
    for idx, score in doc["lsa"]["neighbors"]:
        if score < threshold:
            break
        neighbors.append((int(idx), score))
    neighbors = [(es.get(index=index, id=x, _source=["parsed","lsa.neighbors"])["_source"],s) for x, s in neighbors][1:]
    # build local graph
    root = {}
    root["focused"] = doc["parsed"]
    root["neighbors"] = neighbors
    nodes = [{"name":doc["parsed"]["content"], "group":1}]
    for d, score in neighbors:
        nodes.append({"name":d["parsed"]["content"], "group":2})

    links = []
    for i, (_, score) in enumerate(neighbors):
        links.append({"source":0, "target":i, "value":score})

    return json.dumps({"nodes": nodes, "links": links}, ensure_ascii=False)

def index(request):
    idx = int(request.GET.get('id', 1))
    output = build_doc(idx)
    return HttpResponse(output)
