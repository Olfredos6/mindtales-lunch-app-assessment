from rest_framework.viewsets import ModelViewSet
from core.models import Restaurant, Menu
from core.serializers import RestaurantSerializer, MenuSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
