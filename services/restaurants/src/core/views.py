from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from core.models import Restaurant, Menu
from core.serializers import RestaurantSerializer, MenuSerializer
from core.permissions import IsSuperUser
from rest_framework.decorators import api_view, action
from django.shortcuts import get_object_or_404
import requests
from rest_framework.response import Response
from os import getenv
from uuid import uuid4


MANAGER_BASE_URL = getenv('MANAGER_BASE_URL')


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsSuperUser]


@api_view(http_method_names=['GET', 'PATCH'])
def manager(request, uuid: uuid4) -> Response:
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


@api_view(http_method_names=['GET', 'POST', 'DELETE'])
def menus(request, restaurant_id: uuid4) -> Response:
    '''
        Handles requests to the restaurants/<slug:restaurant_id>/menus
        Implements GET, POST, and DELETE.
        @TODO: Add support for more methods
    '''

    # Handles GET. Returns all menus matching the restaturant 
    # with id restaurant_id
    return Response(
        MenuSerializer(
            Menu.objects.filter(restaurant=restaurant_id),
            many=True
        ).data
    )

# @api_view(http_method_names=['GET', 'POST', 'DELETE'])
# def menus(request, restaurant_id: uuid4, menu_id: uuid4 = None) -> Response:
#     '''
#         Handles requests to the restaurants/<slug:restaurant_id>/menus
#         Implements GET, POST, and DELETE.
#         @TODO: Add support for more methods
#     '''
#     print(f"Received Paramns: Resto {restaurant_id} | Menu: {menu_id}")
   

#     # Handles GET. Returns the menu matching menu_id if sepcified
#     # Otherwise, return all menus matching the restaturant with id
#     # restaurant_id
#     return Response(
#         MenuSerializer(
#             Menu.objects.filter(id=menu_id)
#             if menu_id else
#             Menu.objects.filter(restaurant=restaurant_id),
#             many=False if menu_id else True
#         ).data
#     )
