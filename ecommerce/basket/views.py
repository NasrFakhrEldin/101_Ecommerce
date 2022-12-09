from django.http import JsonResponse
from django.shortcuts import HttpResponse, get_object_or_404, render
from ecommerce.basket.basket import Basket
from ecommerce.inventory.models import Product, ProductInventory


def basket_summary(request):
    return render(request, "basket/basket_summary.html")


def basket_add(request):
    basket = Basket(request)

    if request.POST.get("action") == "post":
        product_web_id = str(request.POST.get("product_web_id"))
        quantity = str(request.POST.get("quantity"))
        product = get_object_or_404(ProductInventory, product__web_id=product_web_id)
        basket.add(product=product, quantity=quantity)
        basket_quantity = basket.__len__()
        response = JsonResponse({"quantity": basket_quantity})
        return response


def basket_delete(request):
    basket = Basket(request)

    if request.POST.get("action") == "post":
        product_web_id = str(request.POST.get("product_web_id"))
        # product = get_object_or_404(ProductInventory, product__web_id=product_web_id)
        # basket.delete(product=product)
        basket.delete(product=product_web_id)
        basket_quantity = basket.__len__()
        response = JsonResponse({"quantity": basket_quantity})
        return response