from rest_framework.routers import DefaultRouter
from core import views
from django.urls import path, include


router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
# router.register(r'restaurants/menus', views.RestaurantViewSet)
# router.register(r'restaurants/', views.RestaurantViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('restaurants/<slug:uuid>/manager', views.manager)
]
