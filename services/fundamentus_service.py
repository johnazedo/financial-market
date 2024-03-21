import pandas as pd
from services.data_service import DataService, SanitizationDataService
import fundamentus


class FundamentusDataService(DataService, SanitizationDataService):

    def get_data_frame(self) -> pd.DataFrame:
        df = fundamentus.get_resultado_raw()
        df = self.filter_data(df, 'Liq.2meses', 'Mrg Ebit')
        df = self.remove_finance_and_insurers(df)
        return df