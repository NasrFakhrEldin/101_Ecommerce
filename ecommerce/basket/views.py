from django.http import JsonResponse
from django.shortcuts import HttpResponse, get_object_or_404, render
from ecommerce.basket.basket import Basket
from ecommerce.inventory.models import ProductInventory


def basket_summary(request):
    basket = Basket(request)

    # Add to Basket
    if request.POST.get("action") == "add":
        product_web_id = int(request.POST.get("product_web_id"))
        quantity = int(request.POST.get("quantity"))
        product = get_object_or_404(ProductInventory, product__web_id=product_web_id)

        basket.add(product=product, quantity=quantity)
        basket_quantity = basket.__len__()
        response = JsonResponse({"quantity": basket_quantity})
        return response

    # Delete from Basket
    if request.POST.get("action") == "delete":
        product_web_id = int(request.POST.get("product_web_id"))

        basket.delete(product=product_web_id)
        basket_quantity = basket.__len__()
        basket_sub_total = basket.get_sub_total_price()
        response = JsonResponse(
            {
                "quantity": basket_quantity,
                "subtotal": basket_sub_total,
            }
        )
        return response

    # Update the Basket
    if request.POST.get("action") == "update":
        product_web_id = int(request.POST.get("product_web_id"))
        quantity = int(request.POST.get("quantity"))

        basket.update(product=product_web_id, quantity=quantity)
        basket_quantity = basket.__len__()
        basket_sub_total = basket.get_sub_total_price()

        response = JsonResponse(
            {
                "quantity": basket_quantity,
                "subtotal": basket_sub_total,
            },
        )
        return response

    return render(request, "basket/basket_summary.html")
