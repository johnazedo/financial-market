import pandas as pd
import fundamentus

FIN_CSV_PATH = "../../data/statusinvest_financas.csv"

class DataRepository():
    def __init__(self, df: pd.DataFrame):
        self._df = df

    def _filter_data(self, liquidity_label: str, ebit_label: str):
        self._df = self._df[self._df[liquidity_label].fillna(0) > 1000000]
        self._df = self._df[self._df[ebit_label].fillna(0) > 0 ]

    def _remove_finance_and_insurers(self):
        fin = pd.read_csv(FIN_CSV_PATH, delimiter=";")
        exclude = fin.loc[:, 'TICKER']
        self._df = self._df[~self._df.index.isin(exclude)]
    
    def get_data_frame(self) -> pd.DataFrame:
        return self._df