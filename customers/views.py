from rest_framework import generics
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomersApiList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer