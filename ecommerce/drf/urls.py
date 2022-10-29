from django.urls import path, include
from rest_framework import routers
from ecommerce.drf import views
from ecommerce.search.views import ProdcutInventorySearch

app_name = "drf"

router = routers.DefaultRouter()

router.register(r"allproduct", views.ProductViewSet, basename="allproduct")
router.register(r"category", views.CategoryViewSet, basename="category")
router.register(
    r"productinventory", views.ProductInventoryViewsSet, basename="productinventory"
)

"""
Main Endpoint
"""

router.register(
    r"product-inventory/(?P<web_id>[^/.]+)",
    views.ProductInventoryByWebId,
    basename="productinventorybycategory",
)

router.register(
    r"product/(?P<slug>[^/.]+)",
    views.ProductByCategory,
    basename="productbycategory",
)

urlpatterns = [
    path("", include(router.urls)),
    path("search/<str:query>/", ProdcutInventorySearch.as_view()),
]
