from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from ecommerce.drf.serializer import (
    ProductSerializer,
    CategorySerializer,
    ProductInventorySerializer,
)

from ecommerce.inventory.models import Category, Product, ProductInventory


class ProductByCategory(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    API endpoint that returns products by category
    """

    queryset = ProductInventory.objects.all()

    def list(self, request, slug=None, *args, **kwargs):
        queryset = ProductInventory.objects.filter(product__category__slug=slug).filter(
            is_default=True
        )[:10]
        serializer = ProductInventorySerializer(
            queryset, context={"request": request}, many=True
        )
        return Response(serializer.data)


"""
just for test
"""


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     lookup_field = "slug"


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"


class ProductInventoryViewsSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# https://www.django-rest-framework.org/api-guide/viewsets/
# https://learnbatta.com/blog/viewsets-in-django-rest-framework-83/
