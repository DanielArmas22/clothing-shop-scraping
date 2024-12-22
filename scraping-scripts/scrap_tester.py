import hym as hym_scraper
print("ejecutando test de hym_scraper")

def test_hym_scraper():
    hym_scraper.iniciar_driver()
    hym_scraper.parametros_busqueda("hombre", 0, "jeans", 10)
    hym_scraper.cargar_url()
    data = hym_scraper.obtener_datos()
    print(data)
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
