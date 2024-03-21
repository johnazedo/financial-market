
from typing import Dict, List


class RankingRepository():
    def get_ev_ebit_ranking(self) -> Dict[str, List[str]]:
        raise NotImplementedError

    def get_roe_ranking(self) -> Dict[str, List[str]]:
        raise NotImplementedError

    def get_list_of_sources(self) -> List[str]:
        raise NotImplementedError
