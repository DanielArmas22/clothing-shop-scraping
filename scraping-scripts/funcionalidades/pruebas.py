import pandas as pd
import dataframe as dataf
import ast
data_df = pd.read_csv("hym_hombre_0_jeans_10.csv")
print(data_df["colores"])
# color_obj = ast.literal_eval(color_str)
# print(color_obj,"tipo",type(color_obj))
producto = data_df.iloc[0]
print(producto)

