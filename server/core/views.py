from django.http import HttpResponse
import elasticsearch
import json

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template

es = elasticsearch.Elasticsearch()


class Graph():
    def __init__(self):
        self.nodes = {}
        self.links = {}
        self.mapping = {}
        self.imax = 0

    def add_node(graph, doc):
        es_id = doc["_id"]
        if es_id in graph.mapping:
            local_id = graph.mapping[es_id]
        else:
            local_id = graph.imax
            graph.imax += 1
            graph.mapping[es_id] = local_id
        graph.nodes[es_id] = {"name": doc["_source"]["parsed"]["content"] ,"es_id": es_id ,"local_id": local_id, "data":doc}
        return graph.nodes[es_id]

    def add_link(graph, n1, n2, score):
        if (n1["local_id"], n2["local_id"]) in graph.links or \
           (n2["local_id"], n1["local_id"]) in graph.links:
            return
        graph.links[(n1["local_id"], n2["local_id"])] = {"source": n1["local_id"],
                                                         "target": n2["local_id"],
                                                         "value": score}

    def extend_graph(graph, doc_id=None):
        if not doc_id:
            doclist = [d["es_id"] for d in graph.nodes.values()]
        else:
            doclist = [doc_id]
        for doc_id in doclist:
            doc = get_doc(doc_id)
            n1 = graph.add_node(doc)
            for d2, score in get_neighbors(doc):
                n2 = graph.add_node(d2)
                graph.add_link(n1, n2, score)

    def to_json(graph):
        # build local graph
        nodes = [{"name": n["name"], "group": 1, "debug":n["local_id"]} for n in sorted(graph.nodes.values(),key=lambda x: x["local_id"])]
        links = [{"source": l["source"], "target":l["target"], "value":l["value"]} for l in graph.links.values()]
        return json.dumps({"nodes": nodes, "links": links}, ensure_ascii=False)



def get_doc(doc_id, index="fumao"):
    return es.get(index=index, id=doc_id)

def get_neighbors(doc, index="fumao", threshold=0.9):
    neighbors = []
    for idx, score in doc["_source"]["lsa"]["neighbors"]:
        if score < threshold:
            break
        neighbors.append((int(idx), score))
    return [(get_doc(x), s) for x, s in neighbors][1:]

def build_graph(idx):
    g = Graph()
    doc = get_doc(idx)
    g.add_node(doc)
    g.extend_graph(doc["_id"])
    for n, score in get_neighbors(doc):
        g.extend_graph(n["_id"])
    g.extend_graph()
    return g.to_json()

def json_api(request):
    idx = int(request.GET.get('id', 1))
    output = build_graph(idx)
    return HttpResponse(output)



def index(request):
    idx = int(request.GET.get('id', 1))
    return render_to_response('index.html', {'idx': idx})
