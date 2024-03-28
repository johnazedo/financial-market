from typing import Dict, List
from services.data_service import DataService
from core.ranking_repository import RankingRepository
from core.model.ticket import TicketInput

class RankingRepositoryImpl(RankingRepository):
    def __init__(self, services: Dict[str, DataService]):
        self.services = services
        self.tickets: Dict[str, TicketInput] = {}
    
    def get_tickets(self, source: str) -> Dict[str, TicketInput]:
        service = self.services[source]

        ev_ebit = service.get_data_frame().sort_values('EV/EBIT')
        roe = service.get_data_frame().sort_values('ROE', ascending=[False])

        pos = 1
        for index, row in ev_ebit.iterrows():
            self.tickets[index] = TicketInput(index, liquidity=row[service.get_liquidity_label()], price=row[service.get_price_label()])
            self.tickets[index].evebit_position = pos
            pos += 1
        
        pos = 1
        for index, row in roe.iterrows():
            self.tickets[index].roe_position = pos
            pos += 1

        return self.tickets