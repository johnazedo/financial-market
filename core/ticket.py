from typing import List


class Ticket():

    def __init__(self, code: str, roe_position: int, evebit_position: int) -> None:
        self.code = code
        self.roe_position = roe_position
        self.evebit_position = evebit_position
    
    def get_magic_formula_score(self):
        return self.roe_position + self.evebit_position


class Ranking():

    class _RankingItem():
        def __init__(self, code: str, position: int) -> None:
            self.code = code
            self.position = position

    def __init__(self) -> None:
        self._store: List[self._RankingItem] = None
    
    def add_item(self, code: str, position: int) -> None:
        item = self._RankingItem(code=code, position=position)
        self._store.append(item)



    