from django.shortcuts import render
from .models import product

# Create your views here.

def base(request):
  return render(request, 'home/base.html')

def products(request):
  products = product.objects.all()

  context = {
    'products' : products,
  }
  return render(request, 'home/product.html', context)


def profile(request):
  context = {
    'profiles' : [
      {'name' : 'Kane Nyamai', 'job' : 'Software Engineer'},
      {'name' : 'Dan Munene', 'job' : 'Data Scientist'},
      {'name' : 'Samuel Ndungu', 'job' : 'Backend Developer'},
      {'name' : 'Joshua Kiteto', 'job' : 'Frontend Developer'},
    ]
  }
  return render(request, 'home/profile.html', context)

