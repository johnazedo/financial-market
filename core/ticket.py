from typing import Dict, List
from config.constants import RANKING_MAX_NUMBER


class Ticket():

    def __init__(self, code: str) -> None:
        self.code = code
        self.roic_position: int = None
        self.evebit_position: int = None
    
    def get_magic_formula_score(self) -> int:
        if(self.roic_position == None or self.evebit_position == None):
            raise ValueError("roic_position or evebit_position were not initialized")
        if(self.roic_position < 0 or self.evebit_position < 0):
            raise ValueError("roic_position or evebit_position were not populate with positive values")
        return self.roic_position + self.evebit_position


class MagicFormulaRanking():
    
    def __init__(self):
        self._tikects: Dict[str, Ticket] = {}
    
    def set_new_roic_position(self, code: str, roic_position: int):
        try:
            self._tikects.get(code).roic_position = roic_position
        except (KeyError, AttributeError) as err: 
            ticket = Ticket(code)
            ticket.roic_position = roic_position
            self._tikects[code] = ticket
    
    def set_new_evebit_position(self, code: str, evebit_position: int):
        try:
            self._tikects.get(code).evebit_position = evebit_position
        except (KeyError, AttributeError) as err: 
            ticket = Ticket(code)
            ticket.evebit_position = evebit_position
            self._tikects[code] = ticket

    def get_result(self) -> List[Ticket]:
        values = self._tikects.values()
        return sorted(values, key=lambda ticket: ticket.get_magic_formula_score())[:RANKING_MAX_NUMBER]
        
