from django.urls import path, include
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    OfferListView,
    OfferDetailView,
    OfferCreateView,
    OfferUpdateView,
    OfferDeleteView,

)
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('/products', views.ProductRESTView)

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="post-detail"),
    path("product/new/", ProductCreateView.as_view(), name="post-create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="post-update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="post-delete"),
    path("offer/", OfferListView.as_view(), name="offer-list"),
    path("offer/<int:pk>/", OfferDetailView.as_view(), name="offer-detail"),
    path("offer/new/", OfferCreateView.as_view(), name="offer-create"),
    path("offer/<int:pk>/update/", OfferUpdateView.as_view(), name="offer-update"),
    path("offer/<int:pk>/delete/", OfferDeleteView.as_view(), name="offer-delete"),
    path("about", views.about),
    path("api", include(router.urls))
]