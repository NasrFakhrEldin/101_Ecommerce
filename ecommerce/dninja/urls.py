from django.urls import path
from ecommerce.dninja.api import api

app_name = "dninja"

urlpatterns = [path("", api.urls)]
