from django.urls import include, path
from ecommerce.basket import views

app_name = "basket"

urlpatterns = [
    path("", views.basket_summary, name="basket_summary"),
    path("add/", views.basket_add, name="basket_add"),
]
