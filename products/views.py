from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def newProduct(request):
    return HttpResponse("New product")


def about(request):
    return render(request, "about.html", {"text": "About page test"})
