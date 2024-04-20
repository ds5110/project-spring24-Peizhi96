import os
import pandas as pd
from typing import Callable, List, Tuple

# groundfish species
# GROUND_FISH = ["COD, ATLANTIC", 
#              "HADDOCK", 
#              "FLOUNDER, YELLOWTAIL", 
#              "POLLOCK", 
#              "FLOUNDER, AMERICAN PLAICE", 
#              "FLOUNDER, WITCH", 
#              "HAKE, WHITE", 
#              "WINDOWPANE", 
#              "FLOUNDER, WINTER", 
#              "REDFISH, ACADIAN", 
#              "HALIBUT, ATLANTIC", 
#              "WOLFFISH, ATLANTIC",
#              "POUT, OCEAN"]

GROUND_FISH = ["COD",
               "HADDOCK",
               "FLOUNDER",
               "POLLOCK",
               "HAKE",
               "WINDOWPANE",
               "REDFISH",
               "HALIBUT",
               "WOLFFISH",
               "POUT"]


def preprocess(filename: str, 
               rowskip: int=0,
               filters: List[Callable[[pd.DataFrame], pd.Series]]=None, 
               converters: List[Tuple[str, Callable[[pd.Series], pd.Series]]]=None,
               modifiers: List[Tuple[str, str, Callable[[pd.DataFrame], pd.Series]]]=None
               ) -> pd.DataFrame:
    df = pd.read_csv(f"data/{filename}", skiprows=rowskip)
    # remove na rows
    df = df.dropna()

    df.sort_values('Year', ascending=True, inplace=True)

    # apply filter
    if filters is not None:
        for filter in filters:
            df = df[filter(df).astype(bool)]

    # apply conversions 
    if converters is not None:
        for column, converter in converters:
            df[column] = converter(df[column])

    # apply modifers
    if modifiers is not None:
        for newColumnName, targetColumnName, function in modifiers:
            df[newColumnName] = df.apply(lambda row: function(row, targetColumnName), axis=1)

    return df

class Converter:
    @staticmethod
    def string_to_int_converter(series: pd.Series) -> pd.Series:
        return series.str.replace(',', '').astype(int)
    
    @staticmethod
    def int_to_string_converter(series: pd.Series) -> pd.Series:
        return series.apply(lambda x: '{:,}'.format(x))


class Extractor:
    @staticmethod
    def extract_species(row, targetColumnName: str) -> str:
        for species in GROUND_FISH:
            if species in str(row[targetColumnName]).upper():
                return species
        return 'OTHER'

    @staticmethod
    def extract_unit_kg_to_pound(row, targetColumnName: str) -> int:
        return round(int(row[targetColumnName]) * 2.20462)
    
    @staticmethod
    def extract_value_per_pound(row, targetColumnName: str) -> int:
        return round(int(row[targetColumnName]) / int(row['Pounds']), 1)

def allocate_figures_directory(reportName: str, id: str) -> str:
    directory_name = f"{reportName}_{id}"
    directory_path = os.path.join("figs", directory_name)
    os.makedirs(directory_path, exist_ok=True)

    return directory_path