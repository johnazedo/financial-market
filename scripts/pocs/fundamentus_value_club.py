# %% Import and get dataframe
import fundamentus

df = fundamentus.get_resultado_raw()
df.columns

# %% 
# Remove companies with liquid margin bigger than R$ 200000
# Remove companies with ebit margin less or equal zero
udf = df[ df['Liq.2meses'] > 1000000]
udf = udf[ udf['Mrg Ebit'] > 0 ]

# %% Remove finance and insurers
import pandas as pd

fin = pd.read_csv("../../data/statusinvest_financas.csv", delimiter=";")
exclude = fin.loc[:, 'TICKER']

udf = udf[~udf.index.isin(exclude)]

# %% 
evebit_ranking = udf.sort_values('EV/EBIT').index
counter = 1
for i in range(len(evebit_ranking)):
    print("#{counter}: {paper} -> {ranking}".format(counter=counter, paper=evebit_ranking[i], ranking=counter))
    counter+=1

# %%
