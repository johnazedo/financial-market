from services.dto import FinancialDTO
from services.handlers import *

class ProcessAndFilterDataService():

    def __init__(self):
        self._dto = FinancialDTO()
        self._process: AbstractHandler = None

        liquid_filter = LiquidMarginFilter()
        ebit_filter = EbitMarginFilter()
        financial_filter = FinancialFilter()
        sort_evebit_handler = SortByEvebitHandler()
        sort_roic_handler = SortByRoicHandler()

        sort_evebit_handler.set_next(sort_roic_handler)
        financial_filter.set_next(sort_evebit_handler)
        ebit_filter.set_next(financial_filter)
        liquid_filter.set_next(ebit_filter)

        self._process = liquid_filter

    def execute(self) -> FinancialDTO:
        return self._process.execute(self._dto)
