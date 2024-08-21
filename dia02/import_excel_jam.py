# %%
import pandas as pd
#para o python abrir o arquivo excel tem que estar com openpyxl instalado
# %%
df = pd.read_excel('../data/transactions.xlsx')
df
# %%
df.shape
# %%
df.head()
# %%
df.tail()
# %%
colunas = ['UUID',
           'Points',
           'IdCustomer',
           'DtTransaction']
df = df[colunas]
df
# %%
df.info(memory_usage='deep')
# %%
