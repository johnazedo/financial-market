import pandas as pd
from core.data_repository import DataRepository


class StatusInvestDataRepository(DataRepository):

    def __init__(self):
        self._df = pd.read_csv("../../data/statusinvest.csv", delimiter=";", decimal=",", thousands=".", index_col="TICKER")
        self._filter_data(' LIQUIDEZ MEDIA DIARIA', 'MARGEM EBIT')
        self._remove_finance_and_insurers()