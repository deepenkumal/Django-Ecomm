from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150,verbose_name='Product Name')
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=150,verbose_name='Product Category')
    description = models.TextField(verbose_name='Product Description')
    image = models.CharField(max_length=150)