import pandas as pd
from abc import ABC, abstractmethod
from config.constants import FIN_CSV_PATH

class DataService(ABC):
    
    @abstractmethod
    def get_data_frame(self) -> pd.DataFrame:
        raise NotImplementedError
    
    @abstractmethod
    def get_liquidity_label(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def get_price_label(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def get_ev_ebit_label(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def get_roe_label(self) -> str:
        raise NotImplementedError


class SanitizationDataService():
    def filter_data(self, df: pd.DataFrame, liquidity_label: str, ebit_label: str) -> pd.DataFrame:
        # Only companies with liquidity greater than 1 million
        df = df[df[liquidity_label].fillna(0) > 1000000]
        # Only companies with positive ebit
        df = df[df[ebit_label].fillna(0) > 0 ]
        return df

    def remove_finance_and_insurers(self, df: pd.DataFrame) -> pd.DataFrame:
        fin = pd.read_csv(FIN_CSV_PATH, delimiter=";")
        exclude = fin.loc[:, 'TICKER']
        df = df[~df.index.isin(exclude)]
        return df

    # This method is necessary because the ev/ebit column can have different names
    # in different data sources
    def change_ev_ebit_name(self, name: str):
        pass
    
    # This method is necessary because the roe column can have different names
    # in different data sources
    def change_roe_name(self, name: str):
        pass