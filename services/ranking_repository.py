from typing import Dict, List
from services.data_service import DataService
from core.ranking_repository import RankingRepository

class RankingRepositoryImpl(RankingRepository):
    def __init__(self, services: Dict[str, DataService]):
        self.services = services

    def get_ev_ebit_ranking_by_source(self, source: str) -> List[str]:
        df = self.services[source].get_data_frame()
        return df.sort_values('EV/EBIT').index.tolist()

    def get_roe_ranking_by_source(self, source: str) -> List[str]:
        df = self.services[source].get_data_frame()
        return df.sort_values('ROE', ascending=[False]).index.tolist()
    
    def get_number_of_companies(self, source: str) -> int:
        return len(self.services[source].get_data_frame())