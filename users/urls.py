from django.urls import path
from . import views
from .views import ProfileDetailView



urlpatterns = [
    path("", views.register),
    path("<int:pk>/details", ProfileDetailView.as_view(), name="profile-detail"),
]