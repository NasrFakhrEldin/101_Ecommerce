from django.contrib import admin
from django.urls import path

from ecommerce.demo import views

app_name = "demo"

urlpatterns = [
    path("", views.home, name="home"),
]
