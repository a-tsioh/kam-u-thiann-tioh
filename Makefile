

Data/all.json:
	python fetch_data.py

Data/parsed.json: Data/all.json
	python preprocess.py

Data/parsed_keyword.json: Data/parsed.json
	python extractKeywords.py

Data/parsed_keywords_lsa.json: Data/parsed_keywords.json
	python runLSA.py

indexed: Data/parsed_keywords_lda.json
	python indexing.py
	touch indexed



