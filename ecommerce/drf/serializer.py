from attr import fields
from rest_framework import serializers

from ecommerce.inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttribute,
    ProductInventory,
    ProductAttributeValue,
    ProductType,
    ProductTypeAttribute,
)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]
        read_only = True


# class ProductAttributeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductAttribute
#         exclude = ["id"]


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    # product_attribute = ProductAttributeSerializer(many=False, read_only=True)

    class Meta:
        model = ProductAttributeValue
        depth = 2
        exclude = ["id"]
        read_only = True


# class ProductTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductType
#         fields = ["name"]


# class ProductTypeAtrributeSerializer(serializers.ModelSerializer):
#     # product_attribute = ProductAttributeSerializer(many=False, read_only=True)
#     product_type = ProductTypeSerializer(many=False, read_only=True)

#     class Meta:
#         model = ProductTypeAttribute
#         # depth = 2
#         fields = ["product_type"]


class MediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["img_url", "alt_text"]
        read_only = True
        editable = False

    def get_img_url(self, obj):
        # return self.context["request"].build_absolute_uri(location=None)
        return obj.img_url.url
        # return self.context["request"].build_absolute_uri(location=obj.img_url.url)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug", "is_active"]
        read_only = True


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=True)

    class Meta:
        model = Product
        # fields = ["web_id", "slug", "name", "description", "category"]
        fields = ["name", "web_id"]
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    product = ProductSerializer(many=False, read_only=True)
    media = MediaSerializer(many=True, read_only=True)

    attributes = ProductAttributeValueSerializer(
        source="attribute_values", many=True, read_only=True
    )
    # product_type = ProductTypeSerializer(many=False, read_only=True)
    # retail_price = serializers.DecimalField(
    #      max_digits=5, decimal_places=2
    # )

    class Meta:
        model = ProductInventory

        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "brand",
            "product",
            "is_on_sale",
            "weight",
            "media",
            "attributes",
            "product_type",
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


class ProductInventorySerializerSearch(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
            "brand",
        ]


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
