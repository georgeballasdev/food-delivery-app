from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    # image = models.ImageField(blank=True)
    # reviews
    # location

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=20)
    store = models.ForeignKey(Store, related_name='categories',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    # image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

