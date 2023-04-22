from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomersApiView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        return Response({'posts': CustomerSerializer(customers, many=True).data})

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Customer.objects.create(
            name=request.data['name'],
            content=request.data['content'],
            group_id=request.data['group_id']
        )
        return Response({'post': CustomerSerializer(post_new).data})