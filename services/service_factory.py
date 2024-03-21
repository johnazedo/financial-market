from typing import List, Dict
from services.data_service import DataService
from services.fundamentus_service import FundamentusDataService
from services.status_invest_service import StatusInvestDataService
from services.ranking_repository import RankingRepositoryImpl
from core.ranking_repository import RankingRepository


class ServiceFactory:
    __services = {
        "STATUS_INVEST": StatusInvestDataService(),
        "FUNDAMENTUS": FundamentusDataService()
    }
    
    @staticmethod
    def get_repository() -> RankingRepository:
        return RankingRepositoryImpl(services=ServiceFactory.__services)