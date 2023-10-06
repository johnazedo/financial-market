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
exclude = ['PSSA3', 'PSSA4', 'ITSA3', 'ITSA4', 'ITUB3', 'QUAL3',
           'ITUB4', 'CXSE3', 'BBAS3', 'BBDC4', 'BBDC3', 'BBSE3'] + fin + seg
availables = []

for paper in udf.index:
    if paper not in exclude:
        availables.append(paper)

udf = udf.filter(items = availables, axis = 0)

# %% Create a global ranking
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
