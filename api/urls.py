from django.contrib import admin
from django.urls import path, include, re_path
from customers.views import CustomerAPIList, CustomerAPIUpdate, CustomerAPIDestroy

from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/customers/', CustomerAPIList.as_view()),
    path('api/v1/customers/<int:pk>/', CustomerAPIUpdate.as_view()),
    path('api/v1/customers/<int:pk>/delete/', CustomerAPIDestroy.as_view()),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
