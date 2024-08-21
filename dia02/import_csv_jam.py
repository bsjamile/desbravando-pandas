# %%

import pandas as pd

df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers #o .. está subindo  o nivel do diretorio 

#estamos usando o metodo do pandas, antes estavamos utilizando a classe dataframe e de series
# %%
df_customers.shape #tupla com qtd de linhas e colunas
# %%
df_customers.describe()
# %%
df_customers.info(memory_usage='deep')
# %%
df_customers["Points"].astype(int)
# %%
df_customers.max()
# %%
df_customers.min()
#%%
condicao = df_customers['Points'] > 1000

df_customers[condicao] #retorna onde a condicao é true

#é assim que se faz filtro em pandas
# %%
maximo = df_customers['Points'].max()
condicao = df_customers['Points'] == maximo
df_customers[condicao]
# %%
#mais coomum encontrar nesse formato
condicao = df_customers['Points'] == df_customers['Points'].max()
df_customers[condicao]
# %%
#´é mais comum ainda encontrar nesse formato
df_customers[df_customers['Points'] == df_customers['Points'].max()]
# %%
df_customers[df_customers['Points'] == df_customers['Points'].max()]['Name'].iloc[0]
# %%
condicao = df_customers['Points'] == df_customers['Points'].max()
#a condicao logical é um dataframe igual ao dataframe anterior mas com as linhas filtradas, correspondendo a logical utilizada (nesse caso oo max - maior numero de pontos)

df_maior = df_customers[condicao]

df_maior['Name'].iloc[0]
# %%
df_customers['Points'] + 1000
# %%
df_customers['Points'] * 1000
# %%
df_customers['Points'] == 1000
# %%

condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)

df_1000_2000 = df_customers[condicao] #faz uma referencia aos dados filtrados
df_1000_2000


df_1000_2000['Points'] = df_1000_2000['Points'] + 1000
df_1000_2000

#nao é saudavel criar uma condicao e depois alterar os dados do Dataframe

#caso oo desejjo seja fazer isso, o melhor seriia criar uma copia da condicao
# %%

condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)

df_1000_2000 = df_customers[condicao].copy() #faz uma copia dos dados e separa dos dados da dataframe
df_1000_2000['Points'] = df_1000_2000['Points'] + 1000
df_1000_2000


# %%
df_customers[condicao].describe() 
# %%
a = [ 1,2,3,4]

b=a

print(a) #mesma lista
print(b) #mesma lista

b2 = a.copy() #agr sao duas listas
b.append(5)

print(a)
print(b)
print(b2) #agora sao 2 listas
# %%
#copia e filtro vc nao estará tratando o dado original
#pandas foi feito para analisar os dados que nao seja dados transacionais (em banco de dados)
#pandas é para analise local, de tabelas
#%%
df_customers[['UUID','Name']] 

# %%
df_customers['UUID']#serie
# %%
df_customers[['UUID']]#dataframee de uma unica coluna
# %%
lista = list(df_customers.columns)
lista.sort() #ordenando em ordem alfabetica
lista
df_customers = df_customers[lista]
df_customers
# %%
colunas = df_customers.columns.to_list()
colunas.sort()
colunas
# %%
df_customers = df_customers[colunas] #colocando o dataframe oriiginal em colunas ordenadas em ordem alfabetica
df_customers
# %%
df_customers = df_customers.rename(columns={'Name':'Nome',
                                            'Points':'Pontos'})
#o rename gera um dataframe novo, nao altera o dataframe anterior
df_customers
# %%
df_customers
# %%
df_customers.rename(columns={'UUID':'Id'}, inplace='True')#inplace = True está permitindo que altere o dataframe original e nao crie um novo
df_customers
# %%
