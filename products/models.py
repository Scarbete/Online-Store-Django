from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='static', blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.FloatField(default=0.0)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


class Comment(models.Model):
    text = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
