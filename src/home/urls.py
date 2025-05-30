from django.urls import path
from .views import base, products, profile

urlpatterns = [
  path('', base, name = 'base'),
  path('product/', products, name = 'product'),
  path('profile/', profile, name = 'profile'),

]