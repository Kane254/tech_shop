from django.shortcuts import render

# Create your views here.

def base(request):
  return render(request, 'home/base.html')

def product(request):
  context = {
    'products' : [
      {'name' : 'Apple Watch',
       'price' : 599,
       'description' : 'Aluminium Case, Starlight Sport'},

       {'name' : 'Samsung Galaxy',
        'price' : 799,
        'description' : 'silicon case, 128GB storage 8GB Ram'},
    ]
  }
  return render(request, 'home/product.html')

