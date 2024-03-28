class Ticket():

    def __init__(self, ticket: str, liquidity: int, score: int) -> None:
        self.ticket = ticket
        self.score = score
        self.liquidity = liquidity


class TicketInput():
    
    def __init__(self, ticket: str, liquidity: int, price: float) -> None:
        self.ticket = ticket
        self.liquidity = liquidity
        self.roe_position = 1000
        self.evebit_position = 1000
        self.price = price