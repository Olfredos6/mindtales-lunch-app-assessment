from rest_framework.viewsets import ModelViewSet
from core.models import Restaurant, Menu
from core.serializers import RestaurantSerializer, MenuSerializer
from core.permissions import IsSuperUser
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
import requests
from rest_framework.response import Response
from os import getenv


MANAGER_BASE_URL = getenv('MANAGER_BASE_URL')


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsSuperUser]


@api_view(http_method_names=['GET', 'PATCH'])
def manager(request, uuid):
    '''
        Handles GET and PATCH requests to
        /restaurants/:restaurant-pk/manager
        Any other method should be made through the
        /managers endpoint

        Requests are then forwarded to /managers if a restaurant
        object match was found
    '''
    # get the restaurant object or return 404
    restaurant = get_object_or_404(Restaurant, id=uuid)

    # init objects
    headers = {
        'Authorization': request.user.get("token")
    }

    # Handling of methods
    if request.method == "GET":
        print("---------->", f"{MANAGER_BASE_URL}/{restaurant.manager}")
        response = requests.get(
            f"{MANAGER_BASE_URL}/{restaurant.manager}",
            headers=headers
        )
        if not response.ok:
            return Response({'detail': response.text})
        return Response(response.json())

    return Response(RestaurantSerializer(restaurant).data)


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
