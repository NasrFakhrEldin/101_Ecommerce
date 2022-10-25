from attr import fields
from rest_framework import serializers

from ecommerce.inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    # ProductAttribute,
    ProductInventory,
    ProductAttributeValue,
    ProductType,
    # ProductTypeAttribute,
)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


# class ProductAttributeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductAttribute
#         exclude = ["id"]


class ProductAtrributeValueSerializer(serializers.ModelSerializer):
    # product_attribute = ProductAttributeSerializer(many=False, read_only=True)

    class Meta:
        model = ProductAttributeValue
        depth = 2
        exclude = ["id"]


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ["name"]


# class ProductTypeAtrributeSerializer(serializers.ModelSerializer):
#     # product_attribute = ProductAttributeSerializer(many=False, read_only=True)
#     product_type = ProductTypeSerializer(many=False, read_only=True)

#     class Meta:
#         model = ProductTypeAttribute
#         # depth = 2
#         fields = ["product_type"]


class MediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    def get_img_url(self, obj):
        # return self.context["request"].build_absolute_uri(location=None)
        return self.context["request"].build_absolute_uri(location=obj.img_url.url)

    class Meta:
        model = Media
        fields = ["img_url", "alt_text"]
        read_only = True
        editable = False


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug", "is_active"]


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=True)

    class Meta:
        model = Product
        # fields = ["web_id", "slug", "name", "description", "category"]
        fields = ["name"]
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    # image = MediaSerializer(source="media_product_inventory", many=True, read_only=True)
    # type = ProductTypeSerializer(source="product_type", many=False, read_only=True)
    # attributes = ProductAtrributeValueSerializer(
    #     source="attribute_values", many=True, read_only=True
    # )
    # brand = BrandSerializer(many=False, read_only=True)
    # price = serializers.DecimalField(
    #     source="retail_price", max_digits=5, decimal_places=2
    # )

    class Meta:
        model = ProductInventory

        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
        ]

        # fields = [
        #     "sku",
        #     "price",
        #     "is_default",
        #     "product",
        #     "image",
        #     "type",
        #     "brand",
        #     "attributes",
        #     "store_price",
        # ]

        read_only = True


"""
Django-mptt model serialize with Django REST framework - Django 

use RecursiveField from the djangorestframework-recursive package
(https://github.com/heywbj/django-rest-framework -recursive)

which can be installed via:

pip3 install djangorestframework-recursive

I was able to do it like so:

from rest_framework_recursive.fields import RecursiveField

class MyModelRecursiveSerializer(serializers.Serializer):

    # your other fields

    children = serializers.ListField(
        read_only=True, source='your_get_children_method', child=RecursiveField()
        )

Just be aware that this is potentially expensive,
so you might want to only use this for models whose entries do not change that often and cache the results.

"""
