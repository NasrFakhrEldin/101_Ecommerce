from rest_framework import viewsets, permissions, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from ecommerce.drf.serializer import (
    ProductSerializer,
    CategorySerializer,
    ProductInventorySerializer,
)

from ecommerce.inventory.models import Category, Product, ProductInventory


class ProductInventoryByWebId(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    API endpoint that returns products inventory by web_id
    """

    queryset = ProductInventory.objects.all()

    def list(self, request, web_id=None, *args, **kwargs):
        queryset = ProductInventory.objects.filter(product__web_id=web_id).filter(
            is_default=True
        )[:10]
        # serializer = ProductInventorySerializer(
        #     queryset, context={"request": request}, many=True
        # )
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductByCategory(viewsets.ViewSet):
    """
    API endpoint that returns products by category
    """

    def list(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)
        serializer = ProductSerializer(
            queryset, context={"request": request}, many=True
        )
        return Response(serializer.data)


"""
just for test
"""


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
# https://profil-software.com/blog/development/10-things-you-need-know-effectively-use-django-rest-framework/
# https://github.com/beda-software/drf-writable-nested
# https://testdriven.io/blog/drf-views-part-3/
# https://testdriven.io/blog/django-drf-elasticsearch/
# https://django-elasticsearch-dsl-drf.readthedocs.io/en/latest/\
