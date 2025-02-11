from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from . import models, serializer
from .scripts import hym as hym_scraper 
from .scripts.functions import dataframe_options as df_options
from .scripts.functions import database_options as db_options

from rest_framework.response import Response
from rest_framework import status
import ast
# Create your views here.
class scrape(APIView):
    def get(self, request):
        # print("ejecutando test de hym_scraper")
        hym_scraper.iniciar_driver()
        genre = request.GET.get('genero')
        offer = 0 #dissabled
        productType = request.GET.get('prenda')
        count = 10 #disabled
        hym_scraper.parametros_busqueda(genre, offer, productType, count)
        hym_scraper.cargar_url()
        data = hym_scraper.obtener_datos()
        data = df_options.data_to_dataframe(data)
        
        print("datos guardados \n",data.head)
        for i in range(0,len(data)):

            product = data.iloc[i]
            #validar si el producto ya existe

            # producto creado
            exists, prod = db_options.check_product(product)
            if exists:
                print("El producto ya existe")
                continue
            prod = models.Product.objects.create(
            name = product["nombre"],
            price = float(product["precio"].replace('S/ ', '')) ,
            url = product["enlace"])

            #imagenes creadas
            for imagen in product["imagenes"]:

                #validar si la imagen ya existe
                exists, img = db_options.check_image(imagen)
                if exists:
                    prod.images.add(img)
                    continue
                img = models.Image.objects.create(
                    url = imagen
                )
                prod.images.add(img)
            #colores creados
            if product["colores"] != "[]":
                print(product["colores"])
                print(type(product["colores"]))
                # colores = ast.literal_eval(product["colores"])
                for color in product["colores"]:
                    print(color)
                    #agregar el color si no existe, si existe obtenerlo y asignarlo al producto
                    col = models.Color.objects.create(name = color.get("nombre"),rgb = color.get("rgb")) if db_options.check_color(color.get("nombre")) == False else db_options.get_color(color.get("nombre"))
                    prod.colors.add(col)
        print("datos guardados en la base de datos")
        return Response({'message': 'Datos guardados en la base de datos'}, status=200)
class ImageList(generics.ListCreateAPIView):
    print("ejecutando list")
    queryset = models.Image.objects.all()
    serializer_class = serializer.ImageSerializer
class ProductViewSet(viewsets.ModelViewSet):
    print("ejecutando product")
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer

class ProductFilter(APIView):
    def get(self, request):
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        color = request.GET.get('color')

        filters = {}
        if min_price and max_price:
            filters['price__range'] = (min_price, max_price)
        if color:
            filters['colors__name__icontains'] = color

        products = models.Product.objects.filter(**filters).distinct()
        #** = desempaqueta el diccionario y lo pasa como argumentos a la funcion
        result_count = products.count()
        product_serializer = serializer.ProductSerializer(products, many=True)
        response_data = {
            'result_count': result_count,
            'products': product_serializer.data
        }
        return Response(response_data, status=200)

# class ProductPriceFilter(APIView):
#     def get(self, request):
#         min_price = request.GET.get('min_price')
#         max_price = request.GET.get('max_price')
#         products = models.Product.objects.filter(price__range=(min_price, max_price))
#         result_count = products.count()
#         product_serializer = serializer.ProductSerializer(products, many=True)
#         response_data = {
#             'result_count': result_count,
#             'products': product_serializer.data
#         }
#         return Response(response_data, status=200)
# class ProductColorFilter(APIView):
#     def get(self, request):
#         color = request.GET.get('color')
#         products = models.Product.objects.filter(colors__name=color)
#         result_count = products.count()
#         product_serializer = serializer.ProductSerializer(products, many=True)
#         response_data = {
#             'result_count': result_count,
#             'products': product_serializer.data
#         }
#         return Response(response_data, status=200)