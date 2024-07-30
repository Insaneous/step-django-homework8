from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  related_name='products')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.FloatField(default=0)
    
    def __str__(self) -> str:
        return self.name
    
    
class Store(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    products = models.ManyToManyField(Product, related_name='stores')
    
    def __str__(self) -> str:
        return self.name