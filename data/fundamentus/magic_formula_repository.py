from core.stonk_market_data import Ranking, RankingRepository
import fundamentus

class MagicFormulaRepository(RankingRepository):
    def __init__(self) -> None:
        self.df = None
        self.ranking = Ranking("fundamentus")
        self._load_data()
        self._filter_papers()
        self._remove_financial_papers()
        self._run_magic_formula()
    
    def _load_data(self) -> None:
        self.df = fundamentus.get_resultado_raw()

    def _filter_papers(self) -> None:
        self.df = self.df[self.df['Liq.2meses'] > 1000000]
        self.df = self.df[self.df['Mrg Ebit'] > 0 ]

    def _remove_financial_papers(self) -> None:
        pass

    def _run_magic_formula(self) -> None:
        evebit_ranking = self.df.sort_values('EV/EBIT').index
        roe_ranking = self.df.sort_values('ROE', ascending=[False]).index
        
        for i in range(len(evebit_ranking)):
            paper = evebit_ranking[i]
            self.ranking.set_new_paper(paper, i)
                
        for i in range(len(roe_ranking)):
            paper = roe_ranking[i]
            self.ranking.set_new_paper(paper, i)

    def get_ranking(self) -> Ranking:
        return self.ranking