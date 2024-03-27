from core.ranking_repository import RankingRepository
from typing import List, Dict

class MagicFormula():
    
    def __init__(self, ranking_repository: RankingRepository) -> None:
        self.ranking_repository = ranking_repository
        self.result: Dict[str, int] = {}

    # TODO: Create a data structure for this usecase
    # TODO: Create a database repository for this usecase

    def invoke(self, source: str) -> List[str]:
        evebit_ranking = self.ranking_repository.get_ev_ebit_ranking_by_source(source)
        roe_ranking = self.ranking_repository.get_roe_ranking_by_source(source)
        
        for i in range(self.ranking_repository.get_number_of_companies(source)):
            evebit_ticket = evebit_ranking[i]
            roe_ticket = roe_ranking[i]
            self._calc_position(evebit_ticket, i)
            self._calc_position(roe_ticket, i)
            
        return self.result

    def _calc_position(self, ticket: str, position: int) -> None:
        if ticket not in self.result:
            self.result[ticket] = position
        else:
            self.result[ticket] += position 
