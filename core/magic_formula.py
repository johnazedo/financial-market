from core.ranking_repository import RankingRepository
from typing import List, Dict

class MagicFormula():
    
    def __init__(self, ranking_repository: RankingRepository) -> None:
        self.ranking_repository = ranking_repository
        self.result: Dict[str, int] = {}


    def invoke(self) -> List[str]:

        evebit_ranking_all_sources = self.ranking_repository.get_ev_ebit_ranking()
        roe_ranking_all_sources = self.ranking_repository.get_roe_ranking()

        for sources in self.ranking_repository.get_list_of_sources():
            evebit_ranking = evebit_ranking_all_sources[sources]
            roe_ranking = roe_ranking_all_sources[sources]

            number_of_companies = self.get_number_of_companies(len(roe_ranking), len(evebit_ranking))

            for i in range(number_of_companies):
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
            
    def get_number_of_companies(self, roe_size: int, evebit_size: int) -> int:
        return min(roe_size, evebit_size)
