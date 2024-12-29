from django.db import models

# Create your models here.
class Image(models.Model): #creacion de una tabla imagen para manejar las multiples imagenes de los productos
    url = models.URLField()
    def __str__(self):
        return self.url
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    # stock = models.IntegerField()
    images = models.ManyToManyField(Image) #relacion de muchos a muchos
    url = models.URLField()

    def __str__(self):
        return self.name
