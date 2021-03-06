from abc import ABC

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product, Offer
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer
from django.contrib.auth.models import User


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['name']
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'price', 'stock', 'image_url', 'offer']

    def form_valid(self, form):
        max_prod = 2
        form.instance.author = self.request.user
        prod = len(User.objects.get(id=self.request.user.id).product_set.all())

        if prod > max_prod:
            form.add_error(error=f"You have reached product limit ({max_prod})", field="name")
            return super().form_invalid(form)
        else:
            return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'price', 'stock', 'image_url', 'offer']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class OfferListView(ListView):
    model = Offer
    template_name = 'offers/offer_list.html'
    context_object_name = 'offers'
    ordering = ['code']
    paginate_by = 10


class OfferDetailView(DetailView):
    model = Offer
    template_name = 'offers/offer_detail.html'


class OfferCreateView(LoginRequiredMixin, CreateView):
    model = Offer
    fields = ['code', 'description', 'discount']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class OfferUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Offer
    fields = ['code', 'description', 'discount']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class OfferDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Offer
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, "about.html", {"text": "About page test"})


class ProductRESTView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
