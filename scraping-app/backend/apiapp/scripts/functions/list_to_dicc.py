def convertir_a_diccionarios(ids, nombres, precios, imagenes, enlaces):
    productos = []
    for i in range(len(ids)):
        producto = {
            "id": ids[i],
            "nombre": nombres[i],
            "precio": precios[i],
            "imagenes": imagenes[i],
            "enlace": enlaces[i],
        }
        productos.append(producto)
    return productos
