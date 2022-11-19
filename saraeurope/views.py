from django.shortcuts import render
from .models import *
from config import settings
from django.core.mail import send_mail
import requests





def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    
    response = requests.get(f'https://geolocation-db.com/json/84.54.66.170&position=true')
    ip_data = response.json()
    Ip.objects.create(ip=ip, country=ip_data['country_name'])


def home_page(request):
    get_client_ip(request)
    products = Products.objects.all()
    slider_img = Pictures.objects.filter(action='Slider')
    context = {'products': products, 'slider_img': slider_img}
    return render(request, 'home.html', context)


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        html = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        send_mail(f'Message by {name}', 'Message', settings.EMAIL_HOST_USER, settings.EMAIL,
                  html_message=html,
                  fail_silently=True)

    return render(request, 'contact.html')


def about_page(request):
    about = AboutUs.objects.get(pk=1)
    context = {'about': about}
    return render(request, 'about.html', context)


def gallery_page(request):
    gallery = Pictures.objects.filter(action='Gallery')
    context = {'gallery': gallery}
    return render(request, 'gallery.html', context)


def products_page(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'products.html', context)


def product_detail(request, pk):
    product = Products.objects.get(pk=pk)
    product_imgs = ProductImage.objects.filter(product=product)
    context = {'product': product, 'product_imgs': product_imgs}
    return render(request, 'product_detail.html', context)











