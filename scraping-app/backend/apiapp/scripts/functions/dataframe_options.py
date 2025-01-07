import pandas as pd
import re
def data_to_dataframe(data):
    global data_df 
    data_to_dataframe = {
    "id":data["id"],
    "nombre":data["nombre"],
    "precio":data["precio"],
    "imagenes":data["imagenes"],
    "enlace":data["enlace"],
    "colores":data["colores"],
}
    data_df = pd.DataFrame(data_to_dataframe);
    return data_df
def filtro_nombre(nombre = ""):
    nombre = data_df[data_df["nombre"] == nombre]
    return nombre.to_dict(orient='list')
def filtro_cortes(fit = ""):
    cortes = data_df[data_df["nombre"].str.contains(fit, case=False, na=False,regex=False)]
    return cortes.to_dict(orient='list')
def filtro_precio(precio = ""):
    precio = data_df[data_df["precio"] == precio]
    return precio.to_dict(orient='list')
def get_nombres():
    nombres = data_df.groupby("nombre").count().sort_values(by="nombre").index.tolist()
    return nombres
def get_precios():
    precios = data_df.groupby("precio").count().index
    precios_float = [float(precio.replace('S/ ', '')) for precio in precios]
    precios_float.sort()
    precios_ordenados = [f'S/ {precio:.2f}' for precio in precios_float]
    return precios_ordenados
def get_cortes(nombres):
    # Expresión regular para buscar "corte" + "Fit" en cualquier parte de la cadena
    cortes = set()
    for nombre in nombres:
        patron = r'(\b\w+ Fit\b)'
        coincidencias = re.findall(patron, nombre)
        if coincidencias:
            cortes.add(coincidencias[0])
    return list(cortes)