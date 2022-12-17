from django.urls import include, path
from ecommerce.cbv import views

app_name = "cbv"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "category/<slug:category_slug>",
        views.CategoryProductListView.as_view(),
        name="category_list",
    ),
    path(
        "product/<slug:slug>",
        views.ProductDetialView.as_view(),
        name="product_detail",
    ),
    path(
        "all/categories",
        views.CategoriesListView.as_view(),
        name="categories_list",
    ),
]
