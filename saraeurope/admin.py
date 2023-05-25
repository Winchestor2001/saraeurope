from dataclasses import field
from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from .models import *


class PhotoAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Products)
class ProductsAdmin(TranslationAdmin):
    list_display = ['title', 'img']
    inlines = [PhotoAdmin]

    class Meta:
        model = Products


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Pictures)
class PicturesAdmin(admin.ModelAdmin):
    list_display = ['action']


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    class Meta:
        model = Products


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    class Meta:
        model = Category


@admin.register(Ip)
class IpAdmin(admin.ModelAdmin):
    list_display = ['ip', 'country']
