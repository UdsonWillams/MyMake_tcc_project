from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from customers.api.v1.helper import create_customer, get_customer

from customers.api.v1.serializers import CreateCustomerSerializer, ListCustomerSerializer, ListCustomerSerializerByEmail, UpdateCustomerSerializer
from customers.models import Customer
class CreateCustomerView(GenericAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCustomerSerializer

    def post(self, request, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                response = create_customer(serializer.validated_data)
                return Response(response, status=HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception:
            raise ValueError()

class ListCustomerView(ListAPIView):
    serializer_class = ListCustomerSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.all() 

class UpdateCustomerView(UpdateAPIView):
    serializer_class = UpdateCustomerSerializer
    
    def get_queryset(self):
        return Customer.objects.all() 

class ListCustomerByEmailView(GenericAPIView):
    serializer_class = ListCustomerSerializerByEmail
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        try:
            import ipdb
            ipdb.set_trace()
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                response = get_customer(serializer.validated_data["email"])
                return Response(response, status=HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception:
            raise ValueError(request.data)
