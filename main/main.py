from core.magic_formula import MagicFormula
from services.service_factory import ServiceFactory
from config.constants import RANKING_MAX_NUMBER

def get_magic_formula() -> MagicFormula:
    return MagicFormula(
        ranking_repository=ServiceFactory.get_repository()
    )

def start():
    magic_formula = get_magic_formula()
    result = magic_formula.invoke("FUNDAMENTUS")
    result = sorted(result.items(), key=lambda x: x[1])

    for i in range(len(result)):
        print(f'{i+1} - {result[i][0]}')

