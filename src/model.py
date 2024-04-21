from matplotlib import ticker
from numpy import median
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Tuple
from template_data import DataDesc, ReportData, StatsPair, YearValue
from util import allocate_figures_directory, preprocess, GROUND_FISH, Converter, Extractor

def get_data_frame(startYear: str, endYear: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df_domestic = preprocess(filename='FOSS_landings.csv', 
                        rowskip=1,
                        filters=[lambda df: df['Year'].between(startYear, endYear),
                                lambda df: df['NMFS Name'].isin(GROUND_FISH), 
                                lambda df: df['State'] == 'MAINE' if DOMESTIC_REGION == 'Maine' else pd.Series(True, index=df.index)], 
                        converters=[('Dollars', Converter.string_to_int_converter),
                                    ('Pounds', Converter.string_to_int_converter)],
                        modifiers=[('Species', 'NMFS Name', Extractor.extract_species), 
                                   ('ValuePerPound', 'Dollars', Extractor.extract_value_per_pound)])

    df_north_atlantic = preprocess(filename='ANNUAL_TRADE_YEAR_PRODUCT_COUNTRY.csv',
                                filters=[lambda df: df['Year'].between(startYear, endYear),
                                        lambda df: df['Product Name'].str.contains('|'.join(GROUND_FISH), case=False, na=False)],
                                converters=[('Value (USD)', Converter.string_to_int_converter),
                                           ('Volume (kg)', Converter.string_to_int_converter)],
                                modifiers=[('Species', 'Product Name', Extractor.extract_species), 
                                           ('Pounds', 'Volume (kg)', Extractor.extract_unit_kg_to_pound),
                                           ('ValuePerPound', 'Value (USD)', Extractor.extract_value_per_pound)])
    
    return (df_domestic, df_north_atlantic)

def find_max(df: pd.DataFrame, columnName: str) -> YearValue:
    index = df[columnName].idxmax()
    max_year = df.loc[index, 'Year']
    max_value = df.loc[index, columnName]
    species = df.loc[index, 'Species']

    return YearValue(max_year, species, max_value)

def find_mean(df: pd.DataFrame, columnName: str) -> YearValue:
    mean_value = round(df[columnName].mean())
    year = df.loc[df[columnName].idxmin(), 'Year']
    species = df.loc[df[columnName].idxmin(), 'Species']

    return YearValue(year, species, mean_value)

def find_median(df: pd.DataFrame, columnName: str) -> YearValue:
    median_value = round(median(df[columnName]))
    year = df.loc[df[columnName].idxmin(), 'Year']
    species = df.loc[df[columnName].idxmin(), 'Species']

    return YearValue(year, species, median_value)

def get_value_delta(df: pd.DataFrame, yearColumnName: str, speciesColumnName: str, valueColumnName: str) -> List[DataDesc]:
    # group by year and species and sum the values
    df_grouped = df.groupby([yearColumnName, speciesColumnName])[valueColumnName].sum().reset_index()
    
    # sort DataFrame by year and species columns
    df_sorted = df_grouped.sort_values(by=[yearColumnName, speciesColumnName])
    
    # calculate the change in value from year to year for each species
    df_sorted['Delta'] = df_sorted.groupby([speciesColumnName])[valueColumnName].diff()
    
    value_delta_list: List[DataDesc] = []
    
    for index, row in df_sorted.iterrows():
        year = row[yearColumnName]
        species = row[speciesColumnName]
        delta = row['Delta']
        
        if pd.notna(delta):
            
            # generate description based on the delta value
            if delta >= 0:
                description = "increased"
            else:
                description = "decreased"
            
            value_delta_list.append(DataDesc(year=year, species=species, value=delta, description=description))
    
    return value_delta_list

def get_value_stats(df: pd.DataFrame, valueColumnName: str) -> List[StatsPair]:
    # group by species and calculate mean and median of the values
    df_grouped = df.groupby(['Species'])[valueColumnName].agg(['mean', 'median']).reset_index()
    
    year_value_list: List[StatsPair] = []
    
    for index, row in df_grouped.iterrows():
        species = row['Species']
        mean = round(row['mean'], 1)
        median = round(row['median'], 1)
        
        year_value_list.append(StatsPair(species=species, mean=mean, median=median))
    
    return year_value_list

def plot_market_value_time_series(df: pd.DataFrame, valueColumnName: str, path: str, figureName: str, title: str) -> str:
    plt.figure(figsize=(12, 8))
    plt.title(title)
    sns.lineplot(data=df, x='Year', y=valueColumnName, hue='Species', errorbar=None, marker='o')
    plt.xlabel('Year')
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.ylabel('Market Value (USD)')
    plt.legend(title='Species')
    plt.grid(axis='y')
    plt.tight_layout()

    file_path = f'{path}/{figureName}.png'
    plt.savefig(file_path)
    plt.close()

    return file_path

def plot_market_value_delta_time_series(data: List[DataDesc], path: str, figureName: str, title: str) -> str:
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(12, 8))
    plt.title(title)
    sns.barplot(data=df, x='year', y='value', hue='species')
    plt.xlabel('Year')
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.ylabel('Market Value Delta (USD)')
    plt.legend(title='Species')
    plt.grid(axis='y')
    plt.tight_layout()

    file_path = f'{path}/{figureName}.png'
    plt.savefig(file_path)
    plt.close()

    return file_path

def plot_market_competition(df_domestic: pd.DataFrame, df_na: pd.DataFrame, path: str, figure_name: str) -> str:
    # aggregate data
    domestic_data = df_domestic.groupby(['Year', 'Species'])['Pounds'].sum().reset_index()
    na_data = df_na.groupby(['Year', 'Species'])['Pounds'].sum().reset_index()

    # calculate market value for each region
    domestic_value = df_domestic.groupby('Year')['Dollars'].sum().reset_index()
    na_value = df_na.groupby('Year')['Value (USD)'].sum().reset_index()

    fig, ax1 = plt.subplots(figsize=(12, 8))

    # volume line plot for North Atlantic
    for species, group in na_data.groupby('Species'):
        ax1.plot(group['Year'], group['Pounds'], label=f'North Atlantic - {species}', linestyle='--', marker='s')

    # volume line plot for domestic
    for species, group in domestic_data.groupby('Species'):
        ax1.plot(group['Year'], group['Pounds'], label=f'{DOMESTIC_REGION} - {species}', linestyle='-', marker='o')

    # create a twin axis for market value
    ax2 = ax1.twinx()

    # market value bar plot for North Atlantic
    ax2.bar(na_value['Year'], na_value['Value (USD)'], alpha=0.2, color='orange', label='North Atlantic')
    # market value bar plot for domestic
    ax2.bar(domestic_value['Year'], domestic_value['Dollars'], alpha=0.3, color='green', label=DOMESTIC_REGION)

    # labels and title
    ax1.set_xlabel('Year')
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax1.set_ylabel('Pounds')
    ax2.set_ylabel('Market Value (USD)')
    ax1.set_title(f'{DOMESTIC_REGION} vs North Atlantic Market Competition')

    plt.xticks(rotation=45)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    
    file_path = f'{path}/{figure_name}.png'
    plt.savefig(file_path)
    plt.close()

    return file_path

def table_plot(df_domestic: pd.DataFrame, df_na: pd.DataFrame, path: str, figure_name: str) -> str:
    # calculate market value delta for domestic
    domestic_value = df_domestic.groupby('Year')['Dollars'].sum().reset_index()
    domestic_value[f'{DOMESTIC_REGION} Market Value Delta (USD)'] = domestic_value['Dollars'].diff()

    # calculate market value delta for North Atlantic
    na_value = df_na.groupby('Year')['Value (USD)'].sum().reset_index()
    na_value['North Atlantic Market Value Delta (USD)'] = na_value['Value (USD)'].diff()

    # calculate market volume for domestic
    domestic_volume = df_domestic.groupby('Year')['Pounds'].sum().reset_index()
    domestic_volume[f'{DOMESTIC_REGION} Market Volume (lb)'] = domestic_volume['Pounds']

    # calculate market volume for North Atlantic
    na_volume = df_na.groupby('Year')['Pounds'].sum().reset_index()
    na_volume['North Atlantic Market Volume (lb)'] = na_volume['Pounds']

    # merge the data frames
    table_data = pd.merge(pd.merge(domestic_value[['Year', f'{DOMESTIC_REGION} Market Value Delta (USD)']], na_value[['Year', 'North Atlantic Market Value Delta (USD)']], on='Year', how='outer'),
                          pd.merge(domestic_volume[['Year', f'{DOMESTIC_REGION} Market Volume (lb)']], na_volume[['Year', 'North Atlantic Market Volume (lb)']], on='Year', how='outer'),
                          on='Year', how='outer')
    table_data = table_data.fillna(0)

    # year duration
    table_data['From'] = table_data['Year'].shift(1)
    table_data['To'] = table_data['Year']

    # remove the first row with NaN values
    table_data = table_data.dropna(subset=['From'])

    # format cell values as integers
    cell_text = [
        [
            f'{int(value):,d}' if isinstance(value, (int, float)) and idx != 0 and idx != 1 else f'{int(value):d}'
            for idx, value in enumerate(row)
        ]
        for row in table_data[['From', 'To', f'{DOMESTIC_REGION} Market Value Delta (USD)', 'North Atlantic Market Value Delta (USD)', f'{DOMESTIC_REGION} Market Volume (lb)', 'North Atlantic Market Volume (lb)']].values.tolist()
    ]

    fig, ax = plt.subplots(figsize=(12, 8))

    # calculate the bounding box for the table
    # adjust the height factor as needed
    table_height = len(cell_text) * 0.625
    # adjust the width factor as needed
    table_width = len(cell_text[0]) * 1.0
    bbox = [0.1, 0.1, table_width, table_height]

    # create the table plot
    table = ax.table(cellText=cell_text,
                     rowLabels=['' for _ in range(table_data.shape[0])],
                     colLabels=table_data[['From', 'To', f'{DOMESTIC_REGION} Market Value Delta (USD)', 'North Atlantic Market Value Delta (USD)', f'{DOMESTIC_REGION} Market Volume (lb)', 'North Atlantic Market Volume (lb)']].columns,
                     loc='center',
                     bbox=bbox)

    table.auto_set_font_size(False)
    table.set_fontsize(32)
    table.scale(1, 1)

    # Remove axis
    ax.axis('off')

    # Save the figure
    figure_path = f"{path}/{figure_name}.png"
    plt.savefig(figure_path, bbox_inches='tight')

    return figure_path


def process(data: ReportData) -> None:
    id = data.report_id
    user_input = data.user_input
    
    start_year = user_input.start_year
    end_year = user_input.end_year
    report_name = user_input.report_name

    global DOMESTIC_REGION
    DOMESTIC_REGION = user_input.region

    data.report_title = f'{DOMESTIC_REGION} and North Atlantic Groundfish Market Competition Analysis Report'

    # get dataframe
    df_domestic, df_north_atlantic = get_data_frame(start_year, end_year)

    # fill data
    # domestic max market value
    data.domestic_maximum_market_value = find_max(df_domestic, 'Dollars')
    # mean value
    data.domestic_average_market_value = find_mean(df_domestic, 'Dollars')
    # median value
    data.domestic_median_market_value = find_median(df_domestic, 'Dollars')
    # domestic max market volume
    data.domestic_maximum_market_volume = find_max(df_domestic, 'Pounds')
    # mean volume
    data.domestic_average_market_volume = find_mean(df_domestic, 'Pounds')
    # median volume
    data.domestic_median_market_volume = find_median(df_domestic, 'Pounds')
    # north atlantic market value
    data.na_maximum_market_value = find_max(df_north_atlantic, 'Value (USD)')
    # mean
    data.na_average_market_value = find_mean(df_north_atlantic, 'Value (USD)')
    # median
    data.na_median_market_value = find_median(df_north_atlantic, 'Value (USD)')
    # north atlantic market volume
    data.na_maximum_market_volume = find_max(df_north_atlantic, 'Pounds')
    # mean
    data.na_average_market_volume = find_mean(df_north_atlantic, 'Pounds')
    # median
    data.na_median_market_volume = find_median(df_domestic, 'Pounds')
    # domestic maximun market value per pound
    data.domestic_maximum_market_value_per_pound = find_max(df_domestic, 'ValuePerPound')
    # mean and median
    data.domestic_stats_market_value_per_pound = get_value_stats(df_domestic, 'ValuePerPound')
    # north atlantic market value per pound
    data.na_maximum_market_value_per_pound = find_max(df_north_atlantic, 'ValuePerPound')
    # mean and median
    data.na_stats_market_value_per_pound = get_value_stats(df_north_atlantic, 'ValuePerPound')
    # domestic year to year market value delta
    data.domestic_year_to_year_market_value_delta = get_value_delta(df_domestic, 'Year', 'Species', 'Dollars')
    # north atlantic year to year market value delta
    data.na_year_to_year_market_value_delta = get_value_delta(df_north_atlantic, 'Year', 'Species', 'Value (USD)')

    # figures generate
    path = allocate_figures_directory(report_name, id)
    # domestic market value time series
    data.domestic_market_value_time_series_figure = plot_market_value_time_series(df_domestic, 'Dollars', 
                                                                          path, 
                                                                          f'{DOMESTIC_REGION}_market_value_time_series_figure', 
                                                                          f'Market Value vs Year of Groundfish Species ({DOMESTIC_REGION})')
    # north atlantic market value time series
    data.na_market_value_time_series_figure = plot_market_value_time_series(df_north_atlantic, 'Value (USD)', 
                                                                       path, 
                                                                       'na_market_value_time_series_figure', 
                                                                       'Market Value vs Year of Groundfish Species (North Atlantic)')
    
    # domestic market value delta time series
    data.domestic_market_value_delta_time_series_figure = plot_market_value_delta_time_series(data.domestic_year_to_year_market_value_delta,
                                                                                      path,
                                                                                      f'{DOMESTIC_REGION}_market_value_delta_time_series_figure',
                                                                                      f'Market Value Delta vs Year of Groundfish Species ({DOMESTIC_REGION})')
    # north atlantic market value delta time series
    data.na_market_value_delta_time_series_figure = plot_market_value_delta_time_series(data.na_year_to_year_market_value_delta,
                                                                                      path,
                                                                                      'na_market_value_delta_time_series_figure',
                                                                                      'Market Value Delta vs Year of Groundfish Species (North Atlantic)')
    # domestic vs north atlantic market competition
    data.domestic_na_market_competition_figure = plot_market_competition(df_domestic, 
                                                                            df_north_atlantic,
                                                                                  path,
                                                                                  f'{DOMESTIC_REGION}_na_market_competition_figure')

    # domestic vs north altantic market value delta table
    data.domestic_na_market_value_delta_table_figure = table_plot(df_domestic, 
                                                               df_north_atlantic,
                                                               path,
                                                               f'{DOMESTIC_REGION}_na_market_value_delta_table_figure')