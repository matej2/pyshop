from abc import ABC

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product
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
    fields = ['name', 'price', 'stock', 'image_url']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'price', 'stock', 'image_url']

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


def about(request):
    return render(request, "about.html", {"text": "About page test"})

