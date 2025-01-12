from ... import models as m
def check_color(color):
    #comparar si el color esta en la base de datos
    colores = m.Color.objects.values_list('name', flat=True)
    if color in colores:
        return True
    return False
def get_color(color):
    #obtener el color de la base de datos
    colorcito = m.Color.objects.get(name = color)
    return colorcito
def check_product(producto): 
    #comparar si el producto esta en la base de datos
    products_name = m.Product.objects.values_list('name', flat=True)
    if producto["nombre"] in products_name:
        db_product = m.Product.objects.get(name = producto["nombre"])
        if db_product.price == producto["precio"] and db_product.url == producto["enlace"]:
            return True, db_product
    return False
# def get_product(producto):
#     #obtener el producto de la base de datos
#     db_product = m.Product.objects.get(name = producto["nombre"])
#     return db_product

def check_image(image):
    #comparar si la imagen esta en la base de datos
    images = m.Image.objects.values_list('url', flat=True)
    if image in images:
        db_image = m.Image.objects.get(url = image)
        return True, db_image
    return False