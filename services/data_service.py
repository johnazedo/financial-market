import pandas as pd
import fundamentus

FIN_CSV_PATH = "../../data/statusinvest_financas.csv"

class DataService():
    def __init__(self, df: pd.DataFrame):
        self._df = df

    def _filter_data(self, liquidity_label: str, ebit_label: str):
        self._df = self._df[self._df[liquidity_label].fillna(0) > 1000000]
        self._df = self._df[self._df[ebit_label].fillna(0) > 0 ]

    def _remove_finance_and_insurers(self):
        fin = pd.read_csv(FIN_CSV_PATH, delimiter=";")
        exclude = fin.loc[:, 'TICKER']
        self._df = self._df[~self._df.index.isin(exclude)]

    # This method is necessary because the ev/ebit column can have different names
    # in different data sources
    def _change_ev_ebit_name(self, name: str):
        pass
    
    # This method is necessary because the roe column can have different names
    # in different data sources
    def _change_roe_name(self, name: str):
        pass
    
    def get_data_frame(self) -> pd.DataFrame:
        return self._df