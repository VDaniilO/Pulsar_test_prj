from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import ProductsModel
from .serializers import ProductsSerializers


class ProductView(ListAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['title', 'article']


class ProductByNameView(APIView):
    def get(self, request, prod_name, format=None):
        products = ProductsModel.objects.filter(title=prod_name)
        serializer = ProductsSerializers(products, many=True)
        return Response({'products': serializer.data})
