from django.contrib import admin

from customers.models import Group, Customer

admin.site.register(Group)
admin.site.register(Customer)