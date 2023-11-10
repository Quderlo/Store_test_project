from django.shortcuts import render
from products.models import ProductCategory, Products

# Create your views here.


def index(request):
    context = {
        'title': 'LevkaStore',
    }
    return render(request, 'store/index.html', context)


def products(request):
    context = {
        'title': 'LevkaStore',
        'products': Products.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'store/products.html', context)
