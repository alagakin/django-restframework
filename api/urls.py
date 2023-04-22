from django.contrib import admin
from django.urls import path
from customers.views import CustomersApiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/customers/', CustomersApiView.as_view())
]
