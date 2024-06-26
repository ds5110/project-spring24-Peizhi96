# project-spring24
## GMRI

* Stakeholder
  * [Dr. Kanae Tokunaga](https://gmri.org/our-approach/staff/kanae-tokunaga/), Senior Scientist (ktokunaga@gmri.org),
  [Gulf of Maine Research Institute (GMRI)](http://gmri.org)
* Story
  * The GMRI Coastal and Marine Economics Lab seeks to understand the mechanisms behind
  decisions and behaviors related to coastal and marine resource uses. This project focuses on the groundfish.
  New England is home to a groundfish fishery that produces a variety of whitefish,
  including species that are culturally important, such as cod and haddock. 
  We also import a large amount of whitefish from the Northeast Atlantic. 
  In other words, locally harvested whitefish directly competes with imports from the Northeast Atlantic. 
  We want to understand the market competition and relationships between New England and Northeast Atlantic 
  (e.g., Norway, Iceland, Scotland). 
* Data
  * Global: https://www.sea-ex.com/trading/market.htm
  * Portland Fish Exchange: https://www.pfex.org/price-landing-tool/
  * NOAA Landings and Foreign Trade: https://www.fisheries.noaa.gov/foss/f?p=215:2:5473541341067


## Team Member
Peizhi Yan(Team Leader, Username: Peizhi96), Zhicun Chen, Zican Hao

## Data collection process

### Local fish data:
1.	Go to website [NOAA Landings](https://www.fisheries.noaa.gov/foss/f?p=215:200:2757927145587:::::).
2.	Select ‘Commercial’ for ‘Data Set’.
3.	Select all the years available by clicking on ‘>>’ button.
4.	Select ‘NMFS Regions’ for ‘Region Type’.
5.	Select ‘New England’ for ‘State Landed’.
6.	Select ‘All species’ for ‘Species’.
7.	Select ‘TOTALS BY YEAR/STATE/SPECIES’ for report format.
8.	Click on ‘RUN REPORT’.
9.	Click on ‘Actions’ -> ‘Download’ -> ‘CSV’ -> ‘Download’.
10.	Data file named ‘FOSS_landings.csv’ will be downloaded.

### Imported fish data:
1.	Go to website [NOAA Foreign Trade](https://www.fisheries.noaa.gov/foss/f?p=215:2:2757927145587:::::).
2.	Select ‘Imports’ for ‘Trade Type’.
3.	Select ‘Annual’ for ‘Time range’.
4.	Select all the years available by clicking on ‘>>’ button.
5.	Select ‘Country’ for ‘Geographic Scale’.
6.	Select all the Northeast Atlantic countries: Belgium, Denmark, Finland, France, Germany, Germany(East), Ireland, Iceland, Luxembourg, Netherlands,  Norway, Portugal, Spain, Sweden, Switzerland, United Kingdom.
7.	Select ‘Product’ for ‘Product Type’.
8.	Select ‘GROUNDFISH(ALL)’ for ‘Product’.
9.	Select ‘TOTALS BY YEAR/PRODUCT/COUNTRY’ for report format.
10.	Click on ‘RUN REPORT’.
11.	Click on ‘Actions’ -> ‘Download’ -> ‘CSV’ -> ‘Download’.
12.	Data file named ‘ANNUAL TRADE-YEAR-PRODUCT-COUNTRY.csv’ will be downloaded.

## EDA
Link to EDA:
[EDA](https://github.com/ds5110/project-spring24-Peizhi96/blob/80087e75ecc6f8877140cf9e51a4e2fc19bb4684/EDA.md)


## Technical Documentation
### Running the Report Script
To generate a report, execute the following command:

```bash
make demo_report
```

For customized reports, use:

```bash
make report
```

Follow the on-screen prompts to specify parameters:

```bash
Enter start year: 2000
Enter end year: 2010
Enter report name: MyReport
Enter region (Maine or New England): New England
```

Parameters Explained
- **Start Year**: The beginning year for the report analysis.
- **End Year**: The ending year for the report analysis.
- **Report Name**: Desired name for the report file.
- **Region**: Landing regions, specifically Maine or New England (case sensitive).

**Note**: The expected behavior is for your report to open and display in your browser. In case of any issues, such as user permission errors, manually open or drag the report_name.html file into your browser.

## Challenge
### Data Processing Challenge
The data processing challenge is more formidable than initially anticipated. Ambiguities arise from certain rows within North Atlantic groundfish imports, where combined product names, such as COD/HADDOCK, obscure the identification of a single species. Dropping these rows outright is infeasible, given their significant market value and volume implications. Consequently, we adopt the first-occurring species as the definitive species for analysis.

## Attribution
Our report template draws inspiration from the findings presented in the ["2022 Commercial Fisheries Value Returns to Levels More in Line with Recent Years"](https://www.maine.gov/dmr/news/fri-03032023-1200-2022-commercial-fisheries-value-returns-levels-more-line-recent-years) report by the Maine Department of Marine Resources.