from django.urls import path
from rest_framework import routers
from django.urls import include

from . import views
productRouter = routers.DefaultRouter()
productRouter.register(r'products', views.ProductViewSet, basename='products')
filter_url = 'products/filter'
urlpatterns = [
    path('scrape/', views.scrape.as_view()),
    path('', include(productRouter.urls)),
    path(f'{filter_url}', views.ProductFilter.as_view()),
]
