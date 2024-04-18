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
    report_id: uuid.UUID
    user_input: UserInput
    report_title: str

    maine_maximum_market_value: YearValue
    maine_maximum_market_volumn: YearValue
    na_maximum_market_value: YearValue
    na_maximum_market_volumn: YearValue
    maine__maximum_average_market_value_per_pound: YearValue
    na__maximum_average_market_value_per_pound: YearValue
    maine_year_to_year_market_value_delta: list[DataDesc]
    na_year_to_year_market_value_delta: list[DataDesc]

    # figures
    maine_market_value_time_series_figure: str
    na_market_value_time_series_figure: str
    maine_market_value_delta_time_series_figure: str
    na_market_value_delta_time_series_figure: str
    maine_na_market_value_compete_figure: str
    maine_na_market_volumn_compete_figure: str