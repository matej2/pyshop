from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("new", views.newProduct),
    path("about", views.about)
]