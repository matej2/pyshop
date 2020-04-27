from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Offer(models.Model):
    code = models.CharField(max_length=30)
    discount = models.FloatField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.code


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})