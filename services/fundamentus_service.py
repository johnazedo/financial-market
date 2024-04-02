import pandas as pd
from services.data_service import DataService, SanitizationDataService
import fundamentus


class FundamentusDataService(DataService, SanitizationDataService):

    def __init__(self) -> None:
        super().__init__()
        self.df = fundamentus.get_resultado_raw()
        self.df = self.filter_data(self.df, self.get_liquidity_label(), self.get_mrg_ebit_label())
        self.df = self.remove_finance_and_insurers(self.df)

    def get_liquidity_label(self) -> str:
        return 'Liq.2meses'	
    
    def get_ev_ebit_label(self) -> str:
        return 'EV/EBIT'

    def get_mrg_ebit_label(self) -> str:
        return 'Mrg Ebit'
    
    def get_price_label(self) -> str:
        return 'Cotação'
    
    def get_roe_label(self) -> str:
        return 'ROIC'

    def get_data_frame(self) -> pd.DataFrame:
        return self.df