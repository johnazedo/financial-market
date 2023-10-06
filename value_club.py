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
fin = fundamentus.list_papel_setor(35)
seg = fundamentus.list_papel_setor(38)
exclude = ['PSSA3', 'PSSA4', 'ITSA3', 'ITSA4', 'ITUB3', 
           'ITUB4', 'CXSE3', 'BBAS3', 'BBDC4', 'BBDC3', 'BBSE3'] + fin + seg
availables = []

for paper in udf.index:
    if paper not in exclude:
        availables.append(paper)

udf = udf.filter(items = availables, axis = 0)

# %% 
evebit_ranking = udf.sort_values('EV/EBIT').index
counter = 1
for i in range(len(evebit_ranking)):
    print("#{counter}: {paper} -> {ranking}".format(counter=counter, paper=evebit_ranking[i], ranking=counter))
    counter+=1
