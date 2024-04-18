from dataclasses import dataclass
import uuid

@dataclass
class DataDesc:
    value: float
    description: str

@dataclass
class UserInput:
    start_year: int
    end_year: int
    report_name: str

@dataclass
class YearValue:
    year: int
    value: float

@dataclass
class ReportData:
    def __init__(self, report_id: uuid.UUID, user_input: UserInput):
        self.report_id = report_id
        self.user_input = user_input

        self.report_title: str = ''

        self.maine_maximum_market_value: YearValue = None
        self.maine_maximum_market_volumn: YearValue = None
        self.na_maximum_market_value: YearValue = None
        self.na_maximum_market_volumn: YearValue = None
        self.maine_maximum_average_market_value_per_pound: YearValue = None
        self.na_maximum_average_market_value_per_pound: YearValue = None
        self.maine_year_to_year_market_value_delta: list[DataDesc] = None
        self.na_year_to_year_market_value_delta: list[DataDesc] = None

        # figures
        self.maine_market_value_time_series_figure: str = None
        self.na_market_value_time_series_figure: str = None
        self.maine_market_value_delta_time_series_figure: str = None
        self.na_market_value_delta_time_series_figure: str = None
        self.maine_na_market_value_compete_figure: str = None
        self.maine_na_market_volumn_compete_figure: str = None