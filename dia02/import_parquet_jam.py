# arquivo binario = arquivo que um programa especifico consegue ler
# o excel, por exemplo, tem formatacaaoo, caraceteres diferentes
#parquet = facilita a leitura e melhora o custo de amarzenamento = utilizado mto em bigdata
# %%
import pandas as pd

# %%
df = pd.read_parquet("../data/transactions_cart.parquet")
df
# %%
