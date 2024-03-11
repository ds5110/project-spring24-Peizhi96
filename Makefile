landings:
	python -b src/eda/graph1.py
	python -b src/eda/graph2.py

north_atlantic:
	python src/eda/preprocess.py
	python src/eda/north_eastern_by_year.py
	python src/eda/north_eastern_by_country.py
	python src/eda/north_eastern_by_product.py
