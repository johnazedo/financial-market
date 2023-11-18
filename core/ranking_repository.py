from typing import List

class Ranking:
    def __init__(self, dataset_id: str) -> None:
        self.dataset_id = dataset_id
        self.papers: dict[str, int] = {}

    def set_new_paper(self, paper: str, points: int) -> None:
        if paper not in self.papers.keys:
            self.papers[paper] = 0
        self.papers[paper] += points
    
    def get_papers(self) -> dict[str, int]:
        return self.papers
    
        
class RankingRepository:
    def get_ranking() -> Ranking:
        pass


