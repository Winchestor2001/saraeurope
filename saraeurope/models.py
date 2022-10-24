from distutils.command.upload import upload
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Products(models.Model):
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
   

class ProductImage(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    img = models.FileField(upload_to='product_imgs/')

    def __str__(self):
        return self.product.title




