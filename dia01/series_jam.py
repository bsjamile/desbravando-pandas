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
series_idades = pd.Series(idades)
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
