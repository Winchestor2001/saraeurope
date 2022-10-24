from django.shortcuts import render
from .models import *


def home_page(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def contact_page(request):
    context = {}
    return render(request, 'contact.html')


def about_page(request):
    context = {}
    return render(request, 'about.html')


def gallery_page(request):
    context = {}
    return render(request, 'gallery.html')


def products_page(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def product_detail(request, pk):
    product = Products.objects.get(pk=pk)
    product_imgs = ProductImage.objects.filter(product=product)
    context = {'product': product, 'product_imgs': product_imgs}
    return render(request, 'product_detail.html', context)











