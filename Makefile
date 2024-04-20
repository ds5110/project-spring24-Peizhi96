.PHONY: report

landings:
	python -b src/eda/graph1.py
	python -b src/eda/graph2.py

north_atlantic:
	python src/eda/preprocess.py
	python src/eda/north_eastern_by_year.py
	python src/eda/north_eastern_by_country.py
	python src/eda/north_eastern_by_product.py

demo_report:
	python src/report_generator.py --start_year 1999 --end_year 2022 --report_name "Annual Report" --region "Maine"

report:
	@read -p "Enter start year: " START_YEAR; \
	read -p "Enter end year: " END_YEAR; \
	read -p "Enter report name: " REPORT_NAME; \
	read -p "Enter region (Maine or New England): " REGION; \
	python src/report_generator.py --start_year $$START_YEAR --end_year $$END_YEAR --report_name "$$REPORT_NAME" --region "$$REGION"