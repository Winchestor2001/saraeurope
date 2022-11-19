from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('context',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category',)