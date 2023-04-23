from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from customers.models import Customer, Group
from customers.serializers import CustomerSerializer, GroupSerializer


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(methods=['get'], detail=False)
    def groups(self, request):
        groups = Group.objects.all()
        return Response({'groups': GroupSerializer(groups, many=True).data})

    @action(methods=['get'], detail=True)
    def group(self, request, pk):
        try:
            group = Group.objects.get(pk=pk)
        except:
            return Response({'error': 'not found'})
        return Response({'groups': GroupSerializer(group).data})