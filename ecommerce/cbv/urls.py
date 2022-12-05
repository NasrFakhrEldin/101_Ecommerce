from django.urls import include, path
from ecommerce.cbv import views

app_name = "cbv"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "<slug:category_slug>",
        views.CategoryListView.as_view(),
        name="category_list",
    ),
    path(
        "detail/<slug:slug>",
        views.ProductDetialView.as_view(),
        name="product_detail",
    ),
]
