from services.out import ProcessAndFilterDataService
from services.dto import Ranking, FinancialDTO
from core.ticket import MagicFormulaRanking, Ticket


def start():
    service = ProcessAndFilterDataService()
    dto: FinancialDTO = service.execute()

    use_case = MagicFormulaRanking()
    dto.evebit_ranking.foreach(
        lambda item: use_case.set_new_evebit_position(item.code, item.position)
    )
    dto.roic_ranking.foreach(
        lambda item: use_case.set_new_roic_position(item.code, item.position)
    )

    tickets = use_case.get_result()

    for item in tickets:
        print(f"{item.code} - {item.get_magic_formula_score()}")


    

