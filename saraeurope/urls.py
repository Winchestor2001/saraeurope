from django.urls import path
from . import views


urlpatterns = [
 path('', views.home_page, name='home'),
 path('contact/', views.contact_page, name='contact'),
 path('about/', views.about_page, name='about'),
 path('gallery/', views.gallery_page, name='gallery'),
 path('products/', views.products_page, name='products'),
 path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
]