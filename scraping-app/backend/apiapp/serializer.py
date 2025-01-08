from rest_framework import serializers
from . import models

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True) #indica que se debe usar el imageSerializer para serializar la relacion, many=True indica que es una relacion de muchos a muchos
    colors = ColorSerializer(many=True) #indica que se debe usar el colorSerializer para serializar la relacion, many=True indica que es una relacion de muchos a muchos
    class Meta:
        model = models.Product
        fields = '__all__'