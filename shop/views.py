from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Collection, ProductImage, Type

# Create your views here.


def home(request):
    return render(request, 'shop/index.html')


def collections(request):
    return render(request, 'shop/home.html')


def about(request):
    return render(request, 'shop/lorem.html')


def product_detail(request, id_coll, id_type, id_prod=1):
    product = get_object_or_404(Product, id=id_prod)
    collection = get_object_or_404(Collection, id=id_coll)
    images = ProductImage.objects.filter(product=product)
    type = get_object_or_404(Type, id=id_type)
    products = Product.objects.filter(type=type)
    return render(request, 'shop/product.html', {'product': product, 'collection': collection, 'images': images, 'type': type, "products": products})


def collection_detail(request, id_coll):
    collection = get_object_or_404(Collection, id=id_coll)
    return render(request, 'shop/home.html', {'collection': collection})


def lookbooks(request):
    return render(request, 'shop/lookbook.html')


def lookbook_detail(request, id_lb):
    return render(request, 'shop/lookbook.html')