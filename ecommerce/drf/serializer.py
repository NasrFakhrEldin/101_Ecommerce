from attr import fields
from rest_framework import serializers

from ecommerce.inventory.models import Product


class AllProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"