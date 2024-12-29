from django.urls import path
from . import views
urlpatterns = [
    path('scrape/', views.scrape.as_view(), name='scrape'),
]
