from decimal import Decimal

from ecommerce.inventory.models import ProductInventory


class Basket:
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get("session_key")

        if "session_key" not in request.session:
            basket = self.session["session_key"] = {}
        self.basket = basket

    def save(self):
        self.session.modified = True

    def add(self, product, quantity):
        """
        Adding and updating the users basket session data
        """

        product_web_id = str(product.product.web_id)

        if product_web_id in self.basket:
            self.basket[product_web_id]["quantity"] = quantity
        else:
            self.basket[product_web_id] = {
                "price": str(product.store_price),
                "quantity": int(quantity),
            }
        self.save()

    def update(self, product, quantity):
        """
        Update values in session data
        """

        product_web_id = str(product)

        if product_web_id in self.basket:
            self.basket[product_web_id]["quantity"] = quantity
        self.save()

    def delete(self, product):
        """
        Delete item from session data
        """

        product_web_id = str(product)
        if product_web_id in self.basket:
            del self.basket[product_web_id]
        self.save()

    def __iter__(self):
        """
        Collect the product_web_id in the session data to query the database
        and return products
        """

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
        """
        Get the basket data and count the quantity of items
        """

        return sum(item["quantity"] for item in self.basket.values())

    def get_sub_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.basket.values()
        )