from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Offer(models.Model):
    code = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    discount = models.FloatField()
    date_posted = models.DateTimeField(default=timezone.now)

