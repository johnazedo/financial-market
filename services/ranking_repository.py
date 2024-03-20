from typing import Dict, List
from data_service import DataService
from core.ranking_repository import RankingRepository
from config.constants import NUMBER_OF_COMPANIES

class RankingRepositoryImpl(RankingRepository):
    def __init__(self, services: Dict[str, DataService]):
        self.services = services
    
    def get_ev_ebit_ranking(self) -> Dict[str, List[str]]:
        ranking = {}
        for service_name, service in self.services.items():
            ranking[service_name] = self._get_ev_ebit_ranking_by_source(service_name)
        return ranking

    def get_roe_ranking(self) -> Dict[str, List[str]]:
        ranking = {}
        for service_name, service in self.services.items():
            ranking[service_name] = self._get_roe_ranking_by_source(service_name)
        return ranking

    def _get_ev_ebit_ranking_by_source(self, source: str) -> List[str]:
        return self.services[source].sort_values('EV/EBIT').index.tolist()[:NUMBER_OF_COMPANIES]

    def _get_roe_ranking_by_source(self, source: str) -> List[str]:
        return self.services[source].sort_values('ROE', ascending=[False]).index.tolist()[:NUMBER_OF_COMPANIES]