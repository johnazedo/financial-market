from core.ranking_repository import RankingRepository
from typing import List, Dict

class MagicFormula():
    
    def __init__(self, ranking_repository: RankingRepository) -> None:
        self.ranking_repository = ranking_repository
        self.result: Dict[str, int] = {}

    # TODO: Create a data structure for this usecase
    # TODO: Create a database repository for this usecase

    def invoke(self, source: str) -> List[str]:
        tickets = self.ranking_repository.get_tickets(source)
        return self.result

    def _calc_position(self, ticket: str, position: int) -> None:
        if ticket not in self.result:
            self.result[ticket] = position
        else:
            self.result[ticket] += position 
