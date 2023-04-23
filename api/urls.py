from django.contrib import admin
from django.urls import path, include, reverse
from customers.views import CustomersViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'customers', CustomersViewSet)
print(router.urls)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
