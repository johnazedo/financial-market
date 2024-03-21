import pandas as pd
from services.data_service import DataService, SanitizationDataService
from config.constants import STATUS_INVEST_CSV_PATH

class StatusInvestDataService(DataService, SanitizationDataService):

    def get_data_frame(self) -> pd.DataFrame:
        df = pd.read_csv(STATUS_INVEST_CSV_PATH, delimiter=";", decimal=",", thousands=".", index_col="TICKER")
        df = self.filter_data(df, ' LIQUIDEZ MEDIA DIARIA', 'MARGEM EBIT')
        df = self.remove_finance_and_insurers(df)
        return df
    
    