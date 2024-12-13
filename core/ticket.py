from typing import List


class Ticket():

    def __init__(self, code: str, roe_position: int, evebit_position: int) -> None:
        self.code = code
        self.roe_position = roe_position
        self.evebit_position = evebit_position
    
    def get_magic_formula_score(self):
        return self.roe_position + self.evebit_position


class MagicFormula():
    pass