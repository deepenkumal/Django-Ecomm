from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150,verbose_name='Product Name')
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=150,verbose_name='Product Category')
    description = models.TextField(verbose_name='Product Description')
    #image = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products/images',verbose_name='Product Image' ,default='products/images/image.png')

    def __str__(self):
        return self.name