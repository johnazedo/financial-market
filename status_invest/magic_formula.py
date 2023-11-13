
# %%
import pandas as pd

df = pd.read_csv("statusinvest.csv", delimiter=";", decimal=",", thousands=".", index_col="TICKER")

# %%
# Filter
udf = df[df[' LIQUIDEZ MEDIA DIARIA'].fillna(0) > 1000000]
udf = udf[udf['MARGEM EBIT'].fillna(0) > 0 ]

fin = pd.read_csv("statusinvest_financas.csv", delimiter=";")
exclude = fin.index

udf = udf[~udf.index.isin(exclude)]

# %%
# Global Ranking
evebit_ranking = udf.sort_values('EV/EBIT').index
roe_ranking = udf.sort_values('ROE', ascending=[False]).index
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
