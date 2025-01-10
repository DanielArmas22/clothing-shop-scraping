from ... import models as m
def check_color(color):
    #comparar si el color esta en la base de datos
    colores = m.Color.objects.all()
    if color in colores:
        return True
    return False
def get_color(color):
    #obtener el color de la base de datos
    colores = m.Color.objects.all()
    for col in colores:
        if col.name == color:
            return col
    return None