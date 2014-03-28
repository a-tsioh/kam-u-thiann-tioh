# -*- coding:utf-8 -*-

import json
import codecs
import re

import gensim as gs

datafile = "Data/parsed_keywords.json"


# a simplistic preprocessing function that remove some stopwords
# and return a list of bigrams
# (may try PTT-based unsup segmentation too)
def transform_doc(s):
    return [txt[i:i+2] for txt in re.split("[。，！？?,]", s) for i in range(len(txt) - 1) ]
    #return [s[i:i+2].encode("utf8") for i in range(len(s)-1)]


data = json.load(open(datafile))
verbatims = []

for post in data:
    verbatims.append(transform_doc(post["parsed"]["content"]))

# build a lexicon from the data
dic = gs.corpora.Dictionary(verbatims)

# index the corpus
corpus = [dic.doc2bow(text) for text in verbatims]

# compute and apply tfidf normalisation (the gensim way)
tfidf = gs.models.TfidfModel(corpus)
tfidf_corpus = tfidf[corpus]

# train a 50 topics LSA model and dumping it
model = gs.models.LsiModel(tfidf_corpus, num_topics=50)
model.save("lsa.model")

# transformed corpus and index for similarity measures
idx = gs.similarities.MatrixSimilarity(model[tfidf_corpus])
vect_iter = iter(model[tfidf_corpus])
# idx = gs.similarities.MatrixSimilarity(c2)
for post in data[:2000]:
    vect = next(vect_iter)
    scores = enumerate(idx[vect])
    neighbors = [(float(id), float(s)) for id, s in
                 sorted(scores, key=lambda x: -x[1])[:20]]
    post["lsa"] = {}
    post["lsa"]["vect"] = vect
    post["lsa"]["neighbors"] = neighbors

json.dump(data,
          codecs.open("Data/parsed_keywords_lsa.json", "w", "utf8"),
          ensure_ascii=False, encoding="utf-8")
