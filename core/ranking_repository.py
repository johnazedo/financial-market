
from typing import Dict
from core.model.ticket import TicketInput

class RankingRepository():
    
    def get_tickets(self, source: str) -> Dict[str, TicketInput]:
        raise NotImplementedError