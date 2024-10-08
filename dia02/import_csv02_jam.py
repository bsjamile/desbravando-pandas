#%%
import pandas as pd

df = pd.read_csv('../data/products.csv',
                sep=';',
                # header=None,
                names=['Id','Name','Description']
                )
df
# %%
df.rename(columns={'Name':'Nome', 
                   'Description':'Descrição'
                   }, 
                   inplace=True
         )
df
# %%
df = df.rename(columns={'Name':'Nome',
                        'Description':'Descrição'
                        }
              )
df
# %%
