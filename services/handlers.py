from config.constants import DECIMAL, EBIT_MARGIN_MIN_VALUE, EBIT_MARGIN_COLUMN, DAILY_LIQUIDY_COLUMN, DAILY_LIQUIDY_MIN_VALUE, INDEX_COL, STATUS_INVEST_FINANCIAL_CSV_FILENAME, DELIMITER, THOUSANDS, ROIC_COLUMN, EVEBIT_COLUMN
from config.path_config import get_file_path
from services.chain_of_responsability import AbstractHandler
from services.dto import FinancialDTO
import pandas as pd

class LiquidMarginFilter(AbstractHandler):
    
    def execute(self, dto: FinancialDTO) -> FinancialDTO:
        dto.df = dto.df[dto.df[DAILY_LIQUIDY_COLUMN].fillna(0) > DAILY_LIQUIDY_MIN_VALUE]
        return super().execute(dto)


class EbitMarginFilter(AbstractHandler):

    def execute(self, dto: FinancialDTO) -> FinancialDTO:
        dto.df = dto.df[dto.df[EBIT_MARGIN_COLUMN].fillna(0) > EBIT_MARGIN_MIN_VALUE]
        return super().execute(dto)


class FinancialFilter(AbstractHandler):
    
    def execute(self, dto: FinancialDTO) -> FinancialDTO:
        file_path = get_file_path(STATUS_INVEST_FINANCIAL_CSV_FILENAME)
        financial = pd.read_csv(file_path, delimiter=DELIMITER)
        financial = financial.loc[:, INDEX_COL]

        dto.df = dto.df[~dto.df.index.isin(financial)]
        return super().execute(dto)


class SortByEvebitHandler(AbstractHandler):
    
    def execute(self, dto: FinancialDTO) -> FinancialDTO:
        evebit_index = dto.df.sort_values(EVEBIT_COLUMN).index

        for i, code in enumerate(evebit_index):
            dto.evebit_ranking.add_item(code, i)

        return super().execute(dto)


class SortByRoicHandler(AbstractHandler):
    
    def execute(self, dto):
        roic_index = dto.df.sort_values(ROIC_COLUMN, ascending=[False]).index

        for i, code in enumerate(roic_index):
            dto.roic_ranking.add_item(code, i)

        return super().execute(dto)
