
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()

urlpatterns = [
    path('auth/', include(router.urls)),
    path('auth/token/', obtain_auth_token, name='api_token_auth'),
]
