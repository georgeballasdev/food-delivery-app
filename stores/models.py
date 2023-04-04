from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(blank=True)
    # reviews
    # location

class Menu(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey(Menu, related_name='categories',on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    image = models.ImageField(blank=True)

