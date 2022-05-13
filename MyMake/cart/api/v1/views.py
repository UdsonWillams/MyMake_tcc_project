from cart.api.v1.helper import actualize_cart, devoluting_products, finalize_cart
from cart.models import Carts
from products.models import Products
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CreateCartsSerializer, ConcluirCartsSerializer, ListCartsSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT,HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView, 
    UpdateAPIView,
    DestroyAPIView
)

class CreateCartsView(CreateAPIView):
    serializer_class = CreateCartsSerializer

class ListCartsView(ListAPIView):
    serializer_class = ListCartsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Carts.objects.all()    
        return queryset

class ListCartsByCustomerView(ListAPIView):
    serializer_class = ListCartsSerializer

    def get_queryset(self):
        queryset = Carts.objects.filter(
            customer_id=self.kwargs["pk"]
        )    
        return queryset
class DeleteCartsView(DestroyAPIView):
    serializer_class = ConcluirCartsSerializer

    def get_queryset(self):
        queryset = Carts.objects.all()    
        return queryset

    def delete(self, request, *args, **kwargs):
        try:
            devoluting_status = devoluting_products(kwargs)
            if devoluting_status:
                return Response({"sucess": devoluting_status}, status=HTTP_204_NO_CONTENT)
            else:
                return Response({"sucess": devoluting_status}, status=HTTP_400_BAD_REQUEST)
        except Exception:
            raise ValueError()

class FinalizeCartsView(DestroyAPIView):
    serializer_class = ConcluirCartsSerializer

    def delete(self, request, *args, **kwargs):
        try:
            return Response(finalize_cart(kwargs), status=HTTP_204_NO_CONTENT)
        except Exception:
            return Response({"status": "fail", "error": "aconteceu algum problema, desculpe tente novamente!"}, status=HTTP_400_BAD_REQUEST)

class UpdateCartsView(UpdateAPIView):
    serializer_class = ConcluirCartsSerializer

    def put(self, request, *args, **kwargs):
        try:
            devoluting_status = actualize_cart(url=kwargs, body=request.data)
            if devoluting_status:
                return Response({"sucess": devoluting_status}, status=HTTP_201_CREATED)
            else:
                return Response({"sucess": devoluting_status}, status=HTTP_400_BAD_REQUEST)
        except Exception:
            raise ValueError()
