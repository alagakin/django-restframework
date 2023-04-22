from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from customers.models import Customer


class CustomersApiView(APIView):
    def get(self, request):
        lst = Customer.objects.all().values()
        return Response({'posts': lst})

    def post(self, request):
        post_new = Customer.objects.create(
            name=request.data['name'],
            content=request.data['content'],
            group_id=request.data['group_id']
        )
        return Response({'post': model_to_dict(post_new)})