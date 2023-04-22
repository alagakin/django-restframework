from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomersApiView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        return Response(
            {'posts': CustomerSerializer(customers, many=True).data})

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT is not allowed'})
        try:
            instance = Customer.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializer = CustomerSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE is not allowed'})

        try:
            Customer.objects.get(pk=pk).delete()
        except:
            return Response({'error': 'Object does not exist'})

        return Response({'post': f"deleted customer with ID {pk}"})