from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


# @pytest.mark.usefixtures("create_three_productinventory")
class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username="admin", password="Pas$w0rd")
        self.client.post(
            reverse("basket:basket"),
            {
                "product_web_id": 45425810,
                "quantity": 1,
                "action": "post",
            },
            xhr=True,
        )
        self.client.post(
            reverse("basket:basket"),
            {
                "product_web_id": 45425811,
                "quantity": 2,
                "action": "post",
            },
            xhr=True,
        )

    def test_basket_url(self):
        """
        Test homepage response status
        """

        response = self.client.get(reverse("basket:basket"))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Test adding items to the basket
        """

        response = self.client.post(
            reverse("basket:basket"),
            {
                "product_web_id": 45425812,
                "quantity": 1,
                "action": "post",
            },
            xhr=True,
        )
        self.assertEqual(response.json(), {"quantity": 4})

        response = self.client.post(
            reverse("basket:basket"),
            {
                "product_web_id": 45425811,
                "quantity": 1,
                "action": "post",
            },
            xhr=True,
        )
        self.assertEqual(response.json(), {"quantity": 3})

    def test_basket_delete(self):
        """
        Test deleting items from the basket
        """

        response = self.client.post(
            reverse("basket:basket"),
            {
                "product_web_id": 45425811,
                "action": "post",
            },
            xhr=True,
        )
        self.assertEqual(response.json(), {"quantity": 1, "subtotal": "92.00"})

    def test_basket_update(self):
        """
        Test updating items from the basket
        """
        response = self.client.post(
            reverse("basket:basket"),
            {
                "product_web_id": 45425811,
                "quantity": 1,
                "action": "post",
            },
            xhr=True,
        )
        self.assertEqual(response.json(), {"quantity": 2, "subtotal": "186.00"})


######################################################################

# "id, sku, upc, product_type, product, brand, is_active,
# is_default, retail_price, store_price, sale_price, weight, created_at, updated_at",

# ProductInventory.objects.create(
#     id=1,
#     sku="7633969397",
#     upc="100000000001",
#     product_type=1,
#     product=1,
#     brand=1,
#     is_active=1,
#     is_default=1,
#     retail_price=97.00,
#     store_price=92.00,
#     sale_price=46.00,
#     weight=987,
#     created_at="2021-09-04 22:14:18.279095",
#     updated_at="2021-09-04 22:14:18.279095",
# )
# ProductInventory.objects.create(
#     id=2,
#     sku="6327000212",
#     upc="100000000002",
#     product_type=1,
#     product=1,
#     brand=1,
#     is_active=1,
#     is_default=1,
#     retail_price=99,
#     store_price=94,
#     sale_price=47,
#     weight=947,
#     created_at="2021-09-04 22:14:18.279095",
#     updated_at="2021-09-04 22:14:18.279095",
# )
# ProductInventory.objects.create(
#     id=8616,
#     sku="3880741573",
#     upc="100000008616",
#     product_type=1,
#     product=8616,
#     brand=1,
#     is_active=1,
#     is_default=1,
#     retail_price=89.00,
#     store_price=84.00,
#     sale_price=42.00,
#     weight=929,
#     created_at="2021-09-04 22:14:18.279095",
#     updated_at="2021-09-04 22:14:18.279095",
# )

#     products = convert_to_dot_notation(create_three_productinventory)

#     first_product = products.first_product
#     second_product = products.second_product
#     third_product = products.third_product
