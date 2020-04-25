from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from . import views


urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("product/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("product/new/", PostCreateView.as_view(), name="post-create"),
    path("product/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("product/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("new", views.newProduct),
    path("about", views.about),
]