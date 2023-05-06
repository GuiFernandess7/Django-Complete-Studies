from django.db import models
from fields import ProductIDField, OrderField

class Product(models.Model):
    name = models.CharField(max_length=50)
    productid = ProductIDField()
    # Ordering of product objects
    order = OrderField()

class Category(models.Model):
    name = models.CharField(max_length=50)

