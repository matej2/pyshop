"""pyshop URL Configuration

The `urlpatterns` list routes URLs to templates. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function templates
    1. Add an import:  from my_app import templates
    2. Add a URL to urlpatterns:  path('', templates.home, name='home')
Class-based templates
    1. Add an import:  from other_app.templates import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index_summary, name="home"),
    path("product/", include("products.urls"), name="test"),
    path("register", include("users.urls"), name="register"),
    path("login",  auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout",  auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("profile/", include("users.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
