from typing import Dict, List
from data_service import DataService


class RankingRepository():
    def __init__(self, services: Dict[str, DataService]):
        self.services = services
    
    def get_ev_ebit_ranking(self) -> Dict[str, List[str]]:
        ranking = {}
        for service_name, service in self.services.items():
            ranking[service_name] = self.get_ev_ebit_ranking_by_source(service_name)
        return ranking

    def get_roe_ranking(self) -> Dict[str, List[str]]:
        ranking = {}
        for service_name, service in self.services.items():
            ranking[service_name] = self.get_roe_ranking_by_source(service_name)
        return ranking

    def _get_ev_ebit_ranking_by_source(self, source: str) -> List[str]:
        return self.services[source].sort_values('EV/EBIT').index.tolist()

    def _get_roe_ranking_by_source(self, source: str) -> List[str]:
        return self.services[source].sort_values('ROE', ascending=[False]).index.tolist()