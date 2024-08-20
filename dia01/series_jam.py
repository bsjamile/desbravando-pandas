# %%
import pandas as pd
# %%
idades = [30,42,90,34]
idades
# %%
media = sum(idades)/len(idades)
media
# %%
sum=0
for idade in idades:
    sum = sum + idade
media2 = sum/len(idades)
media2
# %%
total = 0

for i in idades:
    total+=(media - i)**2
variancia = total / (len(idades) - 1)
variancia
# %%
idades
# %%
series_idades = pd.Series(idades)#clase chamada series do pandas 
series_idades
# %%
series_idades.mean()
# %%
var_series =series_idades.var()
var_series
# %%
dv_padrao_series = series_idades.std()
round(dv_padrao_series,2)
# %%
media_series = series_idades.median()
media_series
# %%
moda_series = series_idades.mode()
moda_series
# %%
series_idades.quantile(0.25) #primeiro quartil
# %%
series_idades.describe()
# %%
series_idades.shape #caracteristica, atributo -> shape = tupla que me diz quantas linhas minhas serie tem
# %%
#serie_idade. o que aparece em cubo é um metodo = são verbos, ações
#o restante é atributo = é uma carateristica = sao coisas que minha serie é, carrega
#navegando na lista
idades[1]
# %%
#navenga na serie
series_idades[1]#retorna o index pq ele é 1
# %%
series_idades
# %%
series_idades.index
# %%
#alterando index da serie
series_idades.index = ['t','e','o','c']
# %%
series_idades
# %%
#navegando nos indices novos
series_idades['c']#retorna o index
# %%
series_idades[0]#retorna a posicao
# %%
series_idades.iloc[0]#iloc = retorna a POSICAO

# %%
series_idades.loc['c']#loc = retorna o INDICE
# %%
series_idades.index=[40,10,30,20]
# %%
series_idades
# %%
series_idades.loc[30]#loc = retorna o INDICE
# %%
series_idades.iloc[2]#iloc = retorna a POSICAO
# %%
series_idades.iloc[-1]#iloc = -1 retorna a ULTIMA POSICAO
# %%
series_idades.iloc[2:4]
# %%
series_idades.iloc[0:2] #se a localizacao pra vc for relevante, utilizar o ILOC
# %%
series_idades.loc[30]
# %%
series_idades[30] #mesma coisa do LOC
# %%
series_idades.name = 'idades'
#a serie vem sem nome mas posso colocar um nome nela tipo uma coluna do excel
# %%
series_idades #aprece com nome
# %%
#criando a serie e definindo um nome
series_idades = pd.Series(idades,name='idades')
series_idades
# %%
