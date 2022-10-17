from rest_framework import viewsets, permissions
from ecommerce.drf.serializer import AllProductSerializer

from ecommerce.inventory.models import Product

class AllProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()[:10]
    serializer_class = AllProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]