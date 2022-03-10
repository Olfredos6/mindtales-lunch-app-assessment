from rest_framework.routers import DefaultRouter
from core import views
from django.urls import path, include


router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('restaurants/<slug:uuid>/manager', views.manager),
    path('restaurants/<slug:restaurant_id>/menus', views.menus),
    path(
        'restaurants/<slug:restaurant_id>/menus/<slug:menu_id>',
        views.menu_detail
    )
]
