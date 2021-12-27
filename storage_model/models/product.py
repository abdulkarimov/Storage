from django.db import models
from .category import Category


class Product(models.Model):
    image = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

