import hym as hym_scraper
from functions import pandas
print("ejecutando test de hym_scraper")

def test_hym_scraper():
    hym_scraper.iniciar_driver()
    a = "hombre"
    b = 0
    c = "jeans"
    d = 10
    hym_scraper.parametros_busqueda(a, b, c, d)
    hym_scraper.cargar_url()
    data = hym_scraper.obtener_datos()
    # print(data)
    #guardar datos en un dataframe 
    pandas.data_to_dataframe(data)
    pandas.save_data(f"hym_{a}_{b}_{c}_{d}.csv")
test_hym_scraper()
# a = 12345
# b = str(a)
# print(b[:3])
# data={
#     "id":[],
#     "nombre":[],
#     "precio":[],
#     "imagenes" : [],
#     "enlace":[],
# }
# data_to_dataframe = {
#     "id":data["id"],
#     "nombre":data["nombre"],
#     "precio":data["precio"],
#     "imagenes":data["imagenes"],
#     "enlace":data["enlace"],
# }
# data_df = pd.DataFrame(data_to_dataframe)
