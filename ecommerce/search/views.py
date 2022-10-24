from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from ecommerce.drf.serializer import ProductInventorySerializer
from ecommerce.search.documents import ProductInventoryDocument


class ProdcutInventorySearch(APIView, LimitOffsetPagination):
    productinventory_serializer = ProductInventorySerializer
    search_document = ProductInventoryDocument

    def get(self, request, query):
        try:
            q = Q(
                "multi_match",
                query=query,
                fields=[
                    "id",
                    "sku",
                    "retail_price",
                ],
            )
            search = self.search_document.search().query(q)
            response = search.execute()
            result = self.paginate_queryset(response, request, view=self)
            serializer = self.productinventory_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        except Exception as e:
            return HttpResponse(e, status=500)
