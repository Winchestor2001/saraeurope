from dataclasses import field
from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


# class ArticleAdminForm(forms.ModelForm):
#     context_en = forms.CharField(widget=CKEditorUploadingWidget())
#     context_bs = forms.CharField(widget=CKEditorUploadingWidget())
#     context_ru = forms.CharField(widget=CKEditorUploadingWidget())
#     context_deuch = forms.CharField(widget=CKEditorUploadingWidget())

#     class Meta:
#         model = Article
#         fields = '__all__'

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
