# -*- coding:utf-8 -*-

import json
import codecs

import gensim as gs
from copy import copy

datafile = "Data/parsed_keywords.json"


# a simplistic preprocessing function that remove some stopwords
# and return a list of bigrams
# (may try PTT-based unsup segmentation too)
def transform_doc(s):
    return [s[i:i+2].encode("utf8") for i in range(len(s)-1)]


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
c2 = model[corpus]
idx = gs.similarities.MatrixSimilarity(c2)

for i, post in enumerate(data):
    post["parsed"]["lsa_vect"] = copy(idx[i])

json.dump(data, codecs.open("Data/parsed_keywords_lsa.json", "w", "utf8"), ensure_ascii=False, encoding="utf-8")
