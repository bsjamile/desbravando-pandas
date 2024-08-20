# %%
import pandas as pd
# %%
data = {
    "nome":["teo","nah","lara","maria"],
    "sobrenome":["calvo","ataide","calvo","calvo"],
    "idade":[31,32,31,2]
}

data
# %%
data["idade"]
# %%
#Dataframe é um conjunto de series
df = pd.DataFrame(data)
df
# %%
df['idade'][0] #index 0
# %%
df['idade'].iloc[0]#posicao 0
# %%
type(df['sobrenome'])
# %%
df['sobrenome'].iloc[2]#posicao 2 
# %%
df['sobrenome'][2] #index 2
# %%
type(df.iloc[0]) #se acessar um indice (nesse caso, a primeira linha) do dataframe vai retornar uma serie
# %%
df.iloc[0]#posicao
#linha = o nome da minha serie é 0(indice diferente do 0 da posicao) e os indices é o nome da coluna correspondente(nome, sobrenome, idade)
# %%
df['nome'] #o nome dessa serie é nome
# %%
# Dataframe pandas nada mais é do que um conjunto de series, seja obter as series por meio das linhas ou por meio das colunas
# %%
df
# %%
df.index=[3,2,1,0]
df
# %%
df.loc[0] #retorna o index, o nome da serie vai ser o index=0 
# %%
df.iloc[0]#retorna a posicao o nome da serie vai ser o index (3)
# %%
df.columns #nome das colunas = atributos = tudo que minha serie é/tem
# metodo= ações, tudo que é capaz de fazer
## %%
#serie_idade. o que aparece em cubo é um metodo = são verbos, ações
#o restante é atributo = é uma carateristica = sao coisas que minha serie é, carrega
# %%
df.info() #object = tudo que não é numérico
# %%
df.info(memory_usage="deep") #qnt de memoria consumida
# %%
df.dtypes #indice é o nome da coluna e objeto é tudo que não é numerico
# %%
df.describe() #aplica nas colunas numericas as estatisticas descritivas
# %%
df['peso']=[80,53,65,14]
sumario = df.describe()
sumario
# %%
sumario['peso']['mean']
# %%
sumario['idade']['mean']

# %%
df.head()#cabeça
# %%
df.head(2)
# %%
df.tail()#rabo/ponta
# %%
df.tail(2)
# %%
dados = [10,20,42,9,12,35,24,10,8,14,21]
df2 = pd.DataFrame(dados)
df2.mean()
# %%
df2.std()
# %%
df2.max()
# %%
datas = {
    'nome':['Téo','Nah','Napoleao'],
    'idade':[31,32,14]
}
# %%
df3 = pd.DataFrame(datas)
# %%
df3.columns
# %%
round(df3['idade'].mean(),2)
# %%
df3.tail()
# %%
df3.head()
# %%
df3.describe()
# %%
df3['idade'].name = 'idade'
# %%
df3
# %%
df3['idade']
# %%
df3.Name= 'pessoas'
# %%
df3
# %%
df3.describe()
# %%
df3.Name
# %%
