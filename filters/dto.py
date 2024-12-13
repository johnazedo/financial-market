import pandas as pd
from config.path_config import get_file_path
from config.constants import DELIMITER, DECIMAL, THOUSANDS, INDEX_COL, STATUS_INVEST_CSV_FILENAME
from typing import Dict, List
from core.ticket import Ticket


class FinancialDTO():

    def __init__(self) -> None:
        super.__init__()
        file_path = get_file_path(STATUS_INVEST_CSV_FILENAME)
        self.df = pd.read_csv(file_path, delimiter=DELIMITER, decimal=DECIMAL, thousands=THOUSANDS, index_col=INDEX_COL)
        self.roic_ranking = List
