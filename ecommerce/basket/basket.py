from decimal import Decimal

from ecommerce.inventory.models import ProductInventory


class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get("session_key")

        if "session_key" not in request.session:
            basket = self.session["session_key"] = {}
        self.basket = basket

    def save(self):
        self.session.modified = True

    def add(self, product, quantity):
        product_web_id = product.product.web_id

        if product_web_id not in self.basket:
            self.basket[product_web_id] = {
                "price": str(product.store_price),
                "quantity": int(quantity),
            }
        self.save()

    def delete(self, product):
        product_web_id = product
        if product_web_id in self.basket:
            del self.basket[product_web_id]
        self.save()

    def __iter__(self):
        products_web_ids = self.basket.keys()
        products = ProductInventory.objects.filter(
            is_active=True, product__web_id__in=products_web_ids
        )
        basket = self.basket.copy()

        for product in products:
            basket[str(product.product.web_id)]["product"] = product

        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["quantity"] * item["price"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.basket.values())

    def get_total_price(self):
        sub_price = sum(item["total_price"] for item in self.basket.values())
        return Decimal(sub_price)

    # basket = ""
    # def __init__(self, request):
    #     self.session = request.session

    #     if Basket.basket is "":
    #         if Basket.basket not in self.session:
    #             Basket.basket = self.session['session_key'] = {'num':101} # test value
    #     self.basket = Basket.basket
