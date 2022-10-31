from typing import List
from ninja import NinjaAPI

from ecommerce.dninja.schema import CategorySchema, ProductInventorySchema, ProductSchema
from ecommerce.inventory.models import Category, Product, ProductInventory

api = NinjaAPI()


@api.get("/category/", response=List[CategorySchema])
def category_list(request):
    qs = Category.objects.all()
    return qs

@api.get("/product/{category_slug}/", response=List[ProductSchema])
def product_by_category(request, category_slug: str):
    qs = Product.objects.filter(category__slug=category_slug)
    return qs

@api.get("/product-inventory/{web_id}/", response=List[ProductInventorySchema])
def productinventory_by_web_id(request, web_id: str):
    qs = ProductInventory.objects.filter(product__web_id=web_id)
    return qs