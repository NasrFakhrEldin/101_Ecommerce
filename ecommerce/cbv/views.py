from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from ecommerce.inventory.models import Category, Product, ProductInventory


class HomeView(TemplateView):
    template_name = "cbv/home.html"

    def get(self, request, *args, **kwargs):
        product_list = ProductInventory.objects.all()
        return render(
            request,
            self.template_name,
            {
                "product_list": product_list,
            },
        )


class CategoriesListView(ListView):
    template_name = "cbv/all_categories.html"

    def get(self, request, *args, **kwargs):
        categories_list = Category.objects.all()
        return render(
            request,
            self.template_name,
            {
                "categories_list": categories_list,
            },
        )


class CategoryProductListView(ListView):
    template_name = "cbv/category_list.html"

    def get(self, request, category_slug=None, *args, **kwargs):
        category = get_object_or_404(Category, slug=category_slug)
        products = ProductInventory.objects.filter(product__category=category)
        return render(
            request,
            self.template_name,
            {
                "category": category,
                "products": products,
            },
        )


class ProductDetialView(DetailView):
    template_name = "cbv/product_detail.html"

    def get(self, request, slug=None, *args, **kwargs):
        product = get_object_or_404(
            ProductInventory, product__slug=slug, is_active=True
        )
        return render(
            request,
            self.template_name,
            {
                "product": product,
            },
        )
