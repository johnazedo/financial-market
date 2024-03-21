from typing import Dict, List
from services.data_service import DataService
from core.ranking_repository import RankingRepository

class RankingRepositoryImpl(RankingRepository):
    def __init__(self, services: Dict[str, DataService]):
        self.services = services
    
    def get_ev_ebit_ranking(self) -> Dict[str, List[str]]:
        ranking = {}
        for service_name in self.services.keys():
            ranking[service_name] = self._get_ev_ebit_ranking_by_source(service_name)
        return ranking

    def get_roe_ranking(self) -> Dict[str, List[str]]:
        ranking = {}
        for service_name in self.services.keys():
            ranking[service_name] = self._get_roe_ranking_by_source(service_name)
        return ranking
    
    def get_list_of_sources(self) -> List[str]:
        return list(self.services.keys())

    def _get_ev_ebit_ranking_by_source(self, source: str) -> List[str]:
        df = self.services[source].get_data_frame()
        return df.sort_values('EV/EBIT').index.tolist()

    def _get_roe_ranking_by_source(self, source: str) -> List[str]:
        df = self.services[source].get_data_frame()
        return df.sort_values('ROE', ascending=[False]).index.tolist()