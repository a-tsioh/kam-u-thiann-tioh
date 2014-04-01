kam-u-thiann-tioh
=================

search engine on 臺灣318運動資料


Backend Initialization
-----------------

at repo root directory, do the following:

1. install virtualenv


    pip install virtualenv
    
2. init the env folder, enter virtual environment


    virtualenv env
    
    . env/bin/activate

3. install django and related packages


    pip install -Ur packages.txt


ElasticSearch initialisation
---------------------------------

1. Download from http://www.elasticsearch.org/overview/elkdownloads/

2. run it

    bin/elasticsearch

Data Preprocessing and Indexing
------------------------------------------

    make indexed


Backend Bootstrap
-----------------

at repo root directory, do the following

    . env/bin/activate
    cd server
    ./watch 8000

Now check http://localhost:8000/


JSON API
--------

at the moment, the url http://localhost/json/($es_id)/ can be used to receive a json doc

where ($es_id) is the id of the doc in the Elasticsearch index.


Things to know:

- the format of the json follow the d3js force-directed graph example (http://bl.ocks.org/mbostock/4062045) format.
- it contains a list of nodes and a list of links
- nodes are documents from the elasticsearch db,
- links exist iff two documents are considered similar by the LSA
- list of nodes includes the requested doc (by id), its neighbors, and the neighbors of its neighbors.
- in the json, nodes also have (local) id for the linking and drawing purpose. The Elasticsearch id thus called es_id

In the futur, we may consider adding 2d or 3d coordinates of the returned documents



