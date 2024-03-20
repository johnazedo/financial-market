from core.ranking_repository import RankingRepository
from typing import List, Dict
from config.constants import NUMBER_OF_COMPANIES

class MagicFormula():
    
    def __init__(self, ranking_repository: RankingRepository) -> None:
        self.ranking_repository = ranking_repository
        self.result: Dict[str, int] = {}


    def invoke(self) -> List[str]:
        evebit_ranking = self.ranking_repository.get_ev_ebit_ranking()['STATUSINVEST']
        roe_ranking = self.ranking_repository.get_roe_ranking()['STATUSINVEST']

        for i in range(NUMBER_OF_COMPANIES):
            evebit_ticket = evebit_ranking[i]
            roe_ticket = roe_ranking[i]
            self._calc_position(evebit_ticket, i)
            self._calc_position(roe_ticket, i)
        
        return self.result


    def _calc_position(self, ticket: str, position: int) -> None:
        self.result[ticket] += position 
            

