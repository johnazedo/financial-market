import pandas as pd
from services.data_service import DataService, SanitizationDataService
from config.constants import STATUS_INVEST_CSV_PATH

class StatusInvestDataService(DataService, SanitizationDataService):

    def __init__(self) -> None:
        super().__init__()
        self.df = pd.read_csv(STATUS_INVEST_CSV_PATH, delimiter=";", decimal=",", thousands=".", index_col="TICKER")
        self.df = self.filter_data(self.df, ' LIQUIDEZ MEDIA DIARIA', 'MARGEM EBIT')
        self.df = self.remove_finance_and_insurers(self.df)

    def get_data_frame(self) -> pd.DataFrame:
        return self.df
    
    