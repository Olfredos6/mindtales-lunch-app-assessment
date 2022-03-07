from rest_framework.routers import DefaultRouter
from core import views


router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
# router.register(r'restaurants/menus', views.RestaurantViewSet)
# router.register(r'restaurants/', views.RestaurantViewSet)

urlpatterns = router.urls
