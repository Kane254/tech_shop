from django.urls import path
from .views import base, product

urlpatterns = [
  path('', base, name = 'base'),
  path('product/', product, name = 'product'),
]