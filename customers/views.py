from rest_framework import generics, viewsets
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer