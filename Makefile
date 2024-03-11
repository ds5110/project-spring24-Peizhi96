DATA = $(PWD)/data/ANNUAL_TRADE_YEAR_PRODUCT_COUNTRY.csv

$(DATA):
	mkdir -p data
	if ! grep -q '^data/ANNUAL_TRADE_YEAR_PRODUCT_COUNTRY.csv$$' .gitignore; then \
		echo 'data/ANNUAL_TRADE_YEAR_PRODUCT_COUNTRY.csv' >> .gitignore; \
	fi
	curl -o $(DATA)
	
north_atlantic:
	python src/preprocess.py
	python src/north_eastern_by_year.py
	python src/north_eastern_by_country.py
	python src/north_eastern_by_product.py

