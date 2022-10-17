from django.urls import path, include
from rest_framework import routers
from ecommerce.drf import views

app_name = "drf"

router = routers.DefaultRouter()

router.register(r"allproduct", views.AllProductViewSet, basename="allproduct")

urlpatterns = [path("", include(router.urls)),]
