from dataclasses import dataclass
import uuid

@dataclass
class DataDesc:
    year: str
    species: str
    value: float
    description: str

@dataclass
class UserInput:
    def __init__(self):
        self.start_year = None
        self.end_year = None
        self.report_name = None
        self.region = None

@dataclass
class YearValue:
    year: int
    species: str
    value: float

@dataclass
class ReportData:
    def __init__(self):
        self.report_id: uuid = None
        self.user_input: UserInput = None

        self.report_title: str = None

        self.domestic_maximum_market_value: YearValue = None
        self.domestic_maximum_market_volume: YearValue = None
        self.na_maximum_market_value: YearValue = None
        self.na_maximum_market_volume: YearValue = None
        self.domestic_maximum_market_value_per_pound: YearValue = None
        self.na_maximum_market_value_per_pound: YearValue = None
        self.domestic_year_to_year_market_value_delta: list[DataDesc] = None
        self.na_year_to_year_market_value_delta: list[DataDesc] = None

        # figures
        self.domestic_market_value_time_series_figure: str = None
        self.na_market_value_time_series_figure: str = None
        self.domestic_market_value_delta_time_series_figure: str = None
        self.na_market_value_delta_time_series_figure: str = None
        self.domestic_na_market_competition_figure: str = None
        self.domestic_na_market_value_delta_table_figure: str = None