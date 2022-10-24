# from django_elasticsearch_dsl import Document, fields
# from django_elasticsearch_dsl.registries import registry

# from ecommerce.inventory.models import ProductInventory


# @registry.register_document
# class ProductInventoryDocument(Document):

#     product = fields.ObjectField(properties={"name": fields.TextField()})

#     product_inventory = fields.ObjectField(properties={"units": fields.IntegerField()})

#     class Index:
#         name = "productinventory"

#     class Django:
#         model = ProductInventory
#         fields = [
#             "id",
#             "sku",
#         ]


from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from ecommerce.inventory.models import ProductInventory


@registry.register_document
class ProductInventoryDocument(Document):
    class Index:
        name = "productinventory"

    class Django:
        model = ProductInventory

        fields = [
            "id",
            "sku",
            "retail_price",
        ]
