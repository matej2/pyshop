from django.urls import path
from . import views


urlpatterns = [
    path("", views.register),
    path("view-details", views.profile, name="profile"),
]