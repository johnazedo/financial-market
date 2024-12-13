from config.constants import RANKING_MAX_NUMBER
from filters.out import ProcessAndFilterDataService
from filters.dto import Ranking, FinancialDTO


def start():
    service = ProcessAndFilterDataService()
    dto: FinancialDTO = ProcessAndFilterDataService.execute()




    

