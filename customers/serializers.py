import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from customers.models import Customer


class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    group_id = serializers.IntegerField()

# class CustomerModel:
#     def __init__(self, name, content):
#         self.name = name
#         self.content = content
# def encode():
#     model = CustomerModel('Angelina Jolie', 'woman')
#     model_sr = CustomerSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"name":"Angelina Jolie","content":"woman"}')
#     data = JSONParser().parse(stream)
#     serializer = CustomerSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
