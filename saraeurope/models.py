from distutils.command.upload import upload
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.category


class Products(models.Model):
    filter = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    energy = models.CharField(max_length=255)
    dry_matter = models.CharField(max_length=255)
    proteins = models.CharField(max_length=255)
    total_fat = models.CharField(max_length=255)
    ash = models.CharField(max_length=255)
    crude_fiber = models.CharField(max_length=255)
    carbohydrate = models.CharField(max_length=255)
    img = models.FileField(blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
   

class ProductImage(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    img = models.FileField(upload_to='product_imgs/')

    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


class Pictures(models.Model):
    CHOICES = (
        ('Slider', 'Slider'),
        ('Gallery', 'Gallery'),
    )

    action = models.CharField(choices=CHOICES, max_length=255)
    picture = models.ImageField()

    def __str__(self):
        return self.action
    
    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'


class AboutUs(models.Model):
    context = RichTextUploadingField()

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class Ip(models.Model):
    ip = models.CharField(max_length=100)
    country = models.CharField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.ip, self.country)

    class Meta:
        verbose_name = 'Human'
        verbose_name_plural = 'Humans'
