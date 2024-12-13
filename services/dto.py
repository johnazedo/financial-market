import pandas as pd
from config.path_config import get_file_path
from config.constants import DELIMITER, DECIMAL, THOUSANDS, INDEX_COL, STATUS_INVEST_CSV_FILENAME
from typing import List, Callable

class FinancialDTO():

    def __init__(self) -> None:
        file_path = get_file_path(STATUS_INVEST_CSV_FILENAME)
        self.df = pd.read_csv(file_path, delimiter=DELIMITER, decimal=DECIMAL, thousands=THOUSANDS, index_col=INDEX_COL)
        self.roic_ranking = Ranking()
        self.evebit_ranking = Ranking()


class Ranking():

    class _RankingItem():
        def __init__(self, code: str, position: int) -> None:
            self.code = code
            self.position: int = position

    def __init__(self) -> None:
        self._store: List[self._RankingItem] = []
    
    def add_item(self, code: str, position: int) -> None:
        item = self._RankingItem(code=code, position=position)
        self._store.append(item)

    def foreach(self, lambda_callback: Callable[[_RankingItem], None]) -> None:
        for item in self._store:
            lambda_callback(item)