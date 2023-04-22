from rest_framework import generics
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomersApiView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer