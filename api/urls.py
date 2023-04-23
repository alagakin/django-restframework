from django.contrib import admin
from django.urls import path
from customers.views import CustomersApiView, CustomersApiList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/customers/', CustomersApiList.as_view()),
    path('api/v1/customers/<int:pk>/', CustomersApiView.as_view())

]
