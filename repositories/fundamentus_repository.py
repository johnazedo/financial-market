from core.data_repository import DataRepository


class FundamentusDataRepository(DataRepository):
    
    def __init__(self):
        self._df = fundamentus.get_resultado_raw()
        self._filter_data('Liq.2meses', 'Mrg Ebit')
        self._remove_finance_and_insurers()