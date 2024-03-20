from data_service import DataService
import fundamentus


class FundamentusDataService(DataService):
    
    def __init__(self):
        self._df = fundamentus.get_resultado_raw()
        self._filter_data('Liq.2meses', 'Mrg Ebit')
        self._remove_finance_and_insurers()