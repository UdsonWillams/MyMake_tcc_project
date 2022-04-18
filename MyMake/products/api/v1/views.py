
from products.api.v1.helper import get_product
from products.models import Products
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView, 
    UpdateAPIView,
    DestroyAPIView
)

from .serializers import (
    CreateProductsSerializers,
    ListProductsSerializers,
    UpdateProductsSerializers,
    DeleteProductsSerializer
)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

class CreateProductsView(CreateAPIView):
    """Create products"""
    serializer_class = CreateProductsSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListProductsView(ListAPIView):
    serializer_class = ListProductsSerializers
    
    def get_queryset(self):
        queryset = Products.objects.all()    
        return queryset

class ListProductsByNameView(ListAPIView):
    serializer_class = ListProductsSerializers
    
    def get_queryset(self, name):
        queryset = Products.objects.filter(name=name)    
        return queryset

    def get(self, request, **kwargs):
        try:
            response = get_product(kwargs["str"])
            return Response(response, status=HTTP_200_OK)
        except ValueError:
            return Response({"error":"product not found"}, status=HTTP_400_BAD_REQUEST)
class UpdateProductsView(UpdateAPIView):
    serializer_class = UpdateProductsSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Products.objects.all()    
        return queryset
class DeleteProductsView(DestroyAPIView):
    serializer_class = DeleteProductsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Products.objects.all()    
        return queryset
