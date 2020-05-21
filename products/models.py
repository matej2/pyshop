from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)


class Offer(models.Model):
    code = models.CharField(max_length=30)
    discount = models.FloatField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('offer-detail', kwargs={'pk': self.pk})


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def clean(self):
        max_prod = 2
        curr_usr = get_current_authenticated_user()
        num_prods = len(User.objects.get(id=curr_usr.id).product_set.all())

        if num_prods > max_prod:
            raise ValidationError(_(f'You have too many products ({num_prods}). Remove some of them. '))

        super.clean(self)
