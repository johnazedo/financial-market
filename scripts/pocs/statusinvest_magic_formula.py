
# %%
import pandas as pd

df = pd.read_csv("../../data/statusinvest.csv", delimiter=";", decimal=",", thousands=".", index_col="TICKER")
df.columns

# %%
# Filter
udf = df[df[' LIQUIDEZ MEDIA DIARIA'].fillna(0) > 3000000]
udf = udf[udf['MARGEM EBIT'].fillna(0) > 0 ]

fin = pd.read_csv("../../data/statusinvest_financas.csv", delimiter=";")
exclude = fin.loc[:, 'TICKER']

udf = udf[~udf.index.isin(exclude)]

# %%
# Global Ranking
evebit_ranking = udf.sort_values('EV/EBIT').index
roe_ranking = udf.sort_values('ROIC', ascending=[False]).index
global_ranking = {}

for i in range(len(evebit_ranking)):
    global_ranking[evebit_ranking[i]] = i
        
for i in range(len(roe_ranking)):
    global_ranking[roe_ranking[i]] += i

result = sorted(global_ranking.items(), key=lambda x:x[1])

# %% Show data
counter = 1
for paper, ranking in result:
    print("#{counter}: {paper} -> {ranking}".format(counter=counter, paper=paper, ranking=ranking))
    counter+=1
# %%

