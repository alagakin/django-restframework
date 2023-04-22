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

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.group_id = validated_data.get('group_id', instance.group_id)
        instance.save()
        return instance

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
