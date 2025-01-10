from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from . import models, serializer
from .scripts import hym as hym_scraper 
from .scripts.functions import dataframe_options as df_options
from .scripts.functions import database_options as db_options

from rest_framework.response import Response
from rest_framework import status

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
            # producto creado
            prod = models.Product.objects.create(
            name = product["nombre"],
            price = float(product["precio"].replace('S/ ', '')) ,
            url = product["enlace"],)

            #imagenes creadas
            for imagen in product["imagenes"]:
                img = models.Image.objects.create(
                    url = imagen
                )
            prod.images.add(img)
            
            #colores creados
            colores = product["colores"].replace("'", "").replace("[", "").replace("]", "").split(",")
            for color in colores:
                #agregar el color si no existe, si existe obtenerlo y asignarlo al producto
                col = models.Color.objects.create(name = color) if db_options.check_color(color) == False else db_options.get_color(color)
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
  