import pandas as pd
from services.data_service import DataService, SanitizationDataService
from config.constants import STATUS_INVEST_CSV_PATH

class StatusInvestDataService(DataService, SanitizationDataService):

    def __init__(self) -> None:
        super().__init__()
        self.df = pd.read_csv(STATUS_INVEST_CSV_PATH, delimiter=";", decimal=",", thousands=".", index_col="TICKER")
        self.df = self.filter_data(self.df, self.get_liquidity_label(), self.get_mrg_ebit_label())
        self.df = self.remove_finance_and_insurers(self.df)

    def get_liquidity_label(self) -> str:
        return ' LIQUIDEZ MEDIA DIARIA'
    
    def get_ev_ebit_label(self) -> str:
        return 'EV/EBIT'
    
    def get_mrg_ebit_label(self) -> str:
        return 'MARGEM EBIT'
    
    def get_price_label(self) -> str:
        return 'PRECO'
    
    def get_roe_label(self) -> str:
        return 'ROIC'

    def get_data_frame(self) -> pd.DataFrame:
        return self.df
    
    