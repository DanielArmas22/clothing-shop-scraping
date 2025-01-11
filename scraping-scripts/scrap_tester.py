import hym as hym_scraper
from funcionalidades import dataframe as dataf
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
    data = dataf.data_to_dataframe(data)
    print("datos guardados \n",data.head)
    dataf.save_data(f"hym_{a}_{b}_{c}_{d}.csv")
    print(data.iloc[1])
    # df = pd.read_csv(f"hym_{a}_{b}_{c}_{d}.csv")
    #obtener una fila
    # print(dir(df))
    # for i in range(0,len(df)):
    #     print(df.iloc[i])
test_hym_scraper()

