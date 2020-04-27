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


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def newProduct(request):
    return HttpResponse("New product")


class PostListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    ordering = ['name']


class PostDetailView(DetailView):
    model = Product


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'price', 'stock', 'image_url', 'offer']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
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
    template_name = 'offers/index.html'
    context_object_name = 'offers'
    ordering = ['code']


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

