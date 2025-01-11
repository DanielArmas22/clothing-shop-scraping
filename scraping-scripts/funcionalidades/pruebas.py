import pandas as pd
import dataframe as dataf
import ast
data_df = pd.read_csv("hym_hombre_0_jeans_10.csv")
print(data_df["colores"])
# color_obj = ast.literal_eval(color_str)
# print(color_obj,"tipo",type(color_obj))
color_str = data_df.iloc[0]["colores"]
print(color_str)
print(type(color_str))
color_obj = ast.literal_eval(color_str)
# print(color_obj[0].get("nombre"))
# print("tipo",type(color_obj[0]))

# colores = product["colores"].replace("'", "").replace("[", "").replace("]", "").split(",")




# print(colores)
# colores = set()
# for color in colores:
#         colores.add(color)
# # colors = dataf.get_colores()
#         # colors.add(c) if c != "" else None
# print(list(colores))
# texto = "background-color: rgb(26, 40, 64);"
# textito = texto.split("rgb")[-1].split(";")[0]
# print(textito)
# objetito = []
# objetito.append({
#     "nombre": "negro",
#     "rgb":"dssd",
# })
# co = set()
# co.add(objetito)
# print(co)