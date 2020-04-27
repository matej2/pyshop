from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    OfferListView,
    OfferDetailView,
    OfferCreateView,
    OfferUpdateView,
    OfferDeleteView,

)
from . import views


urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("product/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("product/new/", PostCreateView.as_view(), name="post-create"),
    path("product/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("product/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("offer/", OfferListView.as_view(), name="offer-list"),
    path("offer/<int:pk>/", OfferDetailView.as_view(), name="offer-detail"),
    path("offer/new/", OfferCreateView.as_view(), name="offer-create"),
    path("offer/<int:pk>/update/", OfferUpdateView.as_view(), name="offer-update"),
    path("offer/<int:pk>/delete/", OfferDeleteView.as_view(), name="offer-delete"),
    path("new", views.newProduct),
    path("about", views.about),
]