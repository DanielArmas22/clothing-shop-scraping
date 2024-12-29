from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from . import models, serializer
from .scripts import hym as hym_scraper 
from .scripts.functions import dataframe_options as pandas
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class scrape(APIView):
    def get(self, request):
        # print("ejecutando test de hym_scraper")
        hym_scraper.iniciar_driver()
        a = "hombre"
        b = 0
        c = "camisas"
        d = 10
        hym_scraper.parametros_busqueda(a, b, c, d)
        hym_scraper.cargar_url()
        data = hym_scraper.obtener_datos()
        print("datos obtenidos")
        # print(data)
        #guardar datos en un dataframe 
        data = pandas.data_to_dataframe(data)
        print("datos guardados \n",data.head)
        for i in range(0,len(data)):
            product = data.iloc[i]
            prod = models.Product.objects.create(
            name = product["nombre"],
            price = float(product["precio"].replace('S/ ', '')) ,
            url = product["enlace"],)
            # imagenes = product["imagenes"],

            for imagen in product["imagenes"]:
                img = models.Image.objects.create(
                    url = imagen
                )
            prod.images.add(img)
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
  