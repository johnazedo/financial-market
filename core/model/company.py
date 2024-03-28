from typing import List
from core.model.ticket import Ticket


class Company():
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.tickets: List[Ticket] = []

    def add_ticket(self, ticket: Ticket) -> None:
        self.tickets.append(ticket)

    def get_best_ticket(self) -> Ticket:
        best_ticket = self.tickets[0]
        for ticket in self.tickets:
            if ticket.score > best_ticket.score:
                best_ticket = ticket
        return best_ticket

    def get_position(self) -> int:
        score_sum = 0
        for ticket in self.tickets:
            score_sum += ticket.score
        
        return round(score_sum/len(self.tickets))


