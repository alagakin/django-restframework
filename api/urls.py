from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, \
    TokenObtainPairView

from customers.views import CustomerAPIList, CustomerAPIUpdate, \
    CustomerAPIDestroy, test_view

from rest_framework import routers

urlpatterns = [
    path('', test_view),
    path('admin/', admin.site.urls),
    path('api/v1/customers/', CustomerAPIList.as_view()),
    path('api/v1/customers/<int:pk>/', CustomerAPIUpdate.as_view()),
    path('api/v1/customers/<int:pk>/delete/', CustomerAPIDestroy.as_view()),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
