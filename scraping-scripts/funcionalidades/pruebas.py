import pandas as pd
import dataframe as dataf
data_df = pd.read_csv("hym_hombre_0_jeans_10.csv")
product = data_df.iloc[0]
print(product)
df_colores = data_df["colores"][0]
colores = df_colores.replace("'", "").replace("[", "").replace("]", "").split(",")
print(colores)
colores = set()
for color in colores:
        colores.add(color)
# colors = dataf.get_colores()
        # colors.add(c) if c != "" else None
print(list(colores))
