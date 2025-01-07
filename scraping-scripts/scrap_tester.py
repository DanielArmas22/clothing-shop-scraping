import hym as hym_scraper
from funcionalidades import pandas
import pandas as pd
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
    data = pandas.data_to_dataframe(data)
    print("datos guardados \n",data.head)
    # pandas.save_data(f"hym_{a}_{b}_{c}_{d}.csv")
    # df = pd.read_csv(f"hym_{a}_{b}_{c}_{d}.csv")
    #obtener una fila
    # print(dir(df))
    # for i in range(0,len(df)):
    #     print(df.iloc[i])
test_hym_scraper()

