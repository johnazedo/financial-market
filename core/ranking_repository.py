
from typing import Dict, List


class RankingRepository():
    
    def get_roe_ranking_by_source(self) -> List[str]:
        raise NotImplementedError
    
    def get_ev_ebit_ranking_by_source(self) -> List[str]:
        raise NotImplementedError
    
    def get_number_of_companies(self, source: str) -> int:
        raise NotImplementedError