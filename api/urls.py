from django.contrib import admin
from django.urls import path, include
from customers.views import CustomersViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'customers', CustomersViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))

]
