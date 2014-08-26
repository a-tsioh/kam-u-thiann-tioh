

Data/all.json:
	wget -O Data/all.json http://padnews.linode.caasih.net/json/all/

Data/parsed.json: Data/all.json
	python preprocess.py

Data/parsed_keywords.json: Data/parsed.json
	python extractKeywords.py

Data/parsed_keywords_lsa.json: Data/parsed_keywords.json
	python runLSA.py

indexed: Data/parsed_keywords_lsa.json
	python indexing.py
	touch indexed



