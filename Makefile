<<<<<<< HEAD
<<<<<<< HEAD
DATA = $(PWD)/data/ANNUAL_TRADE_YEAR_PRODUCT_COUNTRY.csv

$(DATA):
	mkdir -p data
	if ! grep -q '^data/ANNUAL_TRADE_YEAR_PRODUCT_COUNTRY.csv$$' .gitignore; then \
		echo 'data/ANNUAL_TRADE_YEAR_PRODUCT_COUNTRY.csv' >> .gitignore; \
	fi
	curl -o $(DATA)
	
north_atlantic:
	python src/eda2/preprocess.py
	python src/eda2/north_eastern_by_year.py
	python src/eda2/north_eastern_by_country.py
	python src/eda2/north_eastern_by_product.py

=======
landings:
	python -b src/eda/graph1.py
	python -b src/eda/graph2.py
>>>>>>> 2eefc649c9c76609930c9a07e670713dff460339
=======
landings:
	python -b src/eda/graph1.py
	python -b src/eda/graph2.py
>>>>>>> 2eefc649c9c76609930c9a07e670713dff460339
