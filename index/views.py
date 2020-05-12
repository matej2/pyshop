from django.shortcuts import render

# Create your templates here.
from django.views.generic import ListView
from products.models import Offer,Product


def index_summary(request):
    return render(request, 'index_summary.html', {
        "offers": Offer.objects.all()[:5],
        "products": Product.objects.all()[:5]
    })
