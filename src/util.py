import pandas as pd
from typing import Callable, List, Tuple

# groundfish species
groudfish = ["COD, ATLANTIC", 
             "HADDOCK", 
             "FLOUNDER, YELLOWTAIL", 
             "POLLOCK", 
             "FLOUNDER, AMERICAN PLAICE", 
             "FLOUNDER, WITCH", 
             "HAKE, WHITE", 
             "WINDOWPANE", 
             "FLOUNDER, WINTER", 
             "REDFISH, ACADIAN", 
             "HALIBUT, ATLANTIC", 
             "WOLFFISH, ATLANTIC",
             "POUT, OCEAN"]

def preprocess(filename: str, 
               filters: List[Callable[[pd.DataFrame], pd.Series]]=None, 
               converters: List[Tuple[str, Callable[[pd.Series], pd.Series]]]=None
               ) -> pd.DataFrame:
    df = pd.read_csv(f"data/{filename}", skiprows=1)
    # remove na rows
    df = df.dropna()

    # apply filter
    if filters is not None:
        for filter in filters:
            df = df[filter]

    # apply conversions 
    if converters is not None:
        for column, converter in converters:
            df[column] = converter(df[column])

    return df

def dollar_converter(series: pd.Series) -> pd.Series:
    return series.str.replace(',', '').astype(int)


