from django.shortcuts import render, get_object_or_404
from store.models import Category,Product

# Create your views here.

def index(request, category_slug=None):
    products = None

    category_page=Category.objects.get(id = category_slug)
    if category_slug != None:
        products = Product.objects.all().filter(category=category_page,avilable=True)

    else:     
        products = Product.objects.all().filter(available=True)
    return render(request, 'index.html',{'products':products})

def product(request):
    return render(request, 'product.html')