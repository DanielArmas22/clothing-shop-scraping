from bs4 import BeautifulSoup
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys
import time
import json

# Comprobar los imports

# Establecer la ubicacion del driver
home_hym = "https://pe.hm.com/"
def iniciar_driver():
    global driver
    ubicacion_driver = ChromeDriverManager().install()
    servicio = Service(ubicacion_driver)
    # Establecer las opciones de navegacion e inicio del driver.
    options = Options()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--window-size=900,1080")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    options.add_argument("--disable-blink-features=AutomationControlled")


    # Parametros al iniciar el driver
    exp_op = [
        "enable-automation",
        "ignore-certificate-errors",
        "disable-popup-blocking",
    ]
    options.add_experimental_option("excludeSwitches", exp_op)

    # Parametros de preferencias
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "intl.accept_languages": ["es-PE", "es"],
        "credentials_enable_service": False,
    }
    options.add_experimental_option("prefs", prefs)

    # Crear el driver
    driver = webdriver.Chrome(service=servicio, options=options)

def parametros_busqueda(g, d, p, c):
    global genero, descuento, prenda, cantidad
    genero = g
    descuento = d
    prenda = p
    cantidad = c


# Cargar la URL de la Pagina
# def cargar_url():
#     home_hym = "https://pe.hm.com/"
#     url_busqueda = f"{home_hym}/{genero}/{prenda}"
#     driver.get(url_busqueda)
def cargar_url():
    ruta = "https://pe.hm.com/{}%20{}?_q={}%{}&map=ft"
    ruta = ruta.format(genero, prenda, genero, prenda)
    driver.get(ruta)
    
def obtener_datos():
    elemento = driver.find_element(By.CSS_SELECTOR, "html")
    for i in range(5):
        elemento.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
    try:
        cantidad_disponible = driver.find_element(By.CSS_SELECTOR, "span.vtex-search-result-3-x-showingProductsCount").text.split("de")[0].strip()
    except Exception as e:
        print("Error al Localizar la cantidad disponible:", e)
        cantidad_disponible = None
        # cantidad_disponible = "No se pudo localizar la cantidad disponible"

    articulos = driver.find_elements(By.TAG_NAME, "article")
    #padre_
    header = {
        "cantidad_disponible": cantidad_disponible if cantidad_disponible else "No se pudo localizar la cantidad disponible",
        "articulos": len(articulos)
    }
    # data = []
    data = {
        "header": header,
        "id":[],
        "nombre":[],
        "precio":[],
        "imagenes" : [],
        "enlace":[],
        "colores":[],
    }

    # data.append(header)
    for articulo in articulos:
        # nombre = articulo.find_element(By.CSS_SELECTOR, "h2").text
        try:
            nombre = WebDriverWait(articulo, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2"))).text
        except Exception as e:
            print("Error al Localizar el nombre:", e)
            nombre = None
        # precio = articulo.find_element(By.CSS_SELECTOR, "span.vtex-product-price-1-x-sellingPrice").text
        try:
            precio = WebDriverWait(articulo, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.vtex-product-price-1-x-sellingPrice"))).text
        except Exception as e:
            print("Error al Localizar el precio:", e)
            precio = None
        
        # imagenes = articulo.find_elements(By.CSS_SELECTOR, "img")
        try:
            imagenes = WebDriverWait(articulo, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img")))
            url = set()
            for imagen in imagenes:
                url.add(imagen.get_attribute("src"))
        except Exception as e:
            print("Error al Localizar las imagenes del articulo :", e)
            imagenes = None
            
        
        #https://pe.hm.com/1183952002/p
        try:
            padre = WebDriverWait(articulo, 5).until(EC.presence_of_element_located((By.XPATH, ".."))).get_attribute("href")
            codProducto = padre.split("/")[-2] #penuultimo elemento
        except Exception as e:
            print("Error al Localizar el enlace del articulo:", e)
            padre = None
            codProducto = None

        #listaColores
        try:
            listaColores = articulo.find_elements(By.CSS_SELECTOR, "li") # obtiene todos los li dentro de cada articulo
            # listaColores = WebDriverWait(articulo, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li"))) # obtiene todos los li dentro de cada articulo
            # print(listaColores)

            colores = list()
            for color in listaColores:
                color = color.find_element(By.CSS_SELECTOR, "a") # obtiene un a dentro de cada li

                #color_rgb = background-color: rgb(26, 40, 64);
                color_rgb = color.find_element(By.CSS_SELECTOR,"div").get_attribute("style").split("rgb")[-1].split(";")[0] # obtiene el rgb del color
                nombre_color = color.get_attribute("title")
                codColor  = color.get_attribute("href").split("/")[-2]
                colores.append({"nombre": nombre_color, "rgb": color_rgb})
        except Exception as e:
            print("Error al Localizar los colores del articulo:", e)
            colores = None
        data["id"].append(codProducto)
        data["nombre"].append(nombre)
        data["precio"].append(precio)
        data["imagenes"].append(list(url))
        data["enlace"].append(padre)
        data["colores"].append(list(colores))
        #----- Adicional -----
        # url_producto(id)
        # adicional = obtener_producto()
        # data["color"].append(adicional["color"])
        # data["material"].append(adicional["material"])
        # data["tallas_disponibles"].append(adicional["tallas_disponibles"])
        # driver.execute_script("window.history.go(-1)")
        # time.sleep(4)
    # Cerrar el driver
    driver.quit()
    return data

def url_producto(id):
    ruta_producto =f"{home_hym}/{id}/p"
    driver.get(ruta_producto)
def obtener_producto():
    producto_adicional={
        "color": None,
        "material": None,
        "tallas_disponibles": [],
    }
    elemento = driver.find_element(By.CSS_SELECTOR, "html")
    for i in range(5):
        elemento.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
    try:
        color = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.hmperu-shelf-1-x-title"))).text
        producto_adicional["color"] = color
    except Exception as e:
        print("Error al Localizar el color:", e)
        color = None
    try:
        material = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), '%')]"))).text
        producto_adicional["material"] = material
    except Exception as e:
        print("Error al Localizar el material:", e)
        material = None
    try:
        # tallas_disponibles = list(set(driver.find_elements(By.CSS_SELECTOR, "div.vtex-store-components-3-x-skuSelectorItem")))
        talla_producto = []
        tallas_disponibles = driver.find_elements(By.CSS_SELECTOR, "div.vtex-store-components-3-x-skuSelectorItem")

        for talla in tallas_disponibles:
            talla_clase = talla.get_attribute("class").split(" ")
            if "div.vtex-store-components-3-x-unavailable--skuselectorpdp" in talla_clase:
                pass
            else:
                talla_disponible =talla.find_element(By.CSS_SELECTOR, "div.vtex-store-components-3-x-skuSelectorItemTextValue--skuselectorpdp").text
                talla_producto.append(talla_disponible)
    except Exception as e:
        print("Error al Localizar las tallas disponibles:", e)
        talla_producto = None
    producto_adicional["tallas_disponibles"] = talla_producto
    return producto_adicional
    # div.hmperu-shelf-1-x-title (CSS Selector para el color)
    #//p[contains(text(), '%')] (XPATH para el material)
    # div.vtex-store-components-3-x-unavailable--skuselectorpdp (CSS Selector para la talla no disponible)
    #div.vtex-store-components-3-x-skuSelectorItem (CSS Selector para las tallas)