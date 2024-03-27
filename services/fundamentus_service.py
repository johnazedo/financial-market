import pandas as pd
from services.data_service import DataService, SanitizationDataService
import fundamentus


class FundamentusDataService(DataService, SanitizationDataService):

    def __init__(self) -> None:
        super().__init__()
        self.df = fundamentus.get_resultado_raw()
        self.df = self.filter_data(self.df, 'Liq.2meses', 'Mrg Ebit')
        self.df = self.remove_finance_and_insurers(self.df)

    def get_data_frame(self) -> pd.DataFrame:
        return self.df