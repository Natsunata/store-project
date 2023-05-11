from django.shortcuts import render
from products.models import ProductCategory, Product

def home(request):
    context = {'title': 'Store'}
    return render(request, 'products\index.html', context)

def products(request):
    context = {'title': 'Store - Каталог',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all(),}
    return render(request, 'products\products.html', context)
