from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from core.models import Restaurant, Menu
from core.serializers import MenuItemSerializer, \
    RestaurantSerializer, MenuSerializer, DetailedMenuSerializer
from core.permissions import IsSuperUser
from django.shortcuts import get_object_or_404
import requests
from os import getenv
from datetime import date

MANAGER_BASE_URL = getenv('MANAGER_BASE_URL')


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsSuperUser]

    @action(methods=['GET'], detail=False)
    def votable_menus(self, request):
        '''
            Returns a list of menus that are votable
        '''
        return Response(
            DetailedMenuSerializer(
                Menu.objects.filter(
                    date_created__date=date.today()
                                    ), many=True
            ).data
        )


@api_view(http_method_names=['GET', 'PATCH'])
def manager(request, uuid: str) -> Response:
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


@api_view(http_method_names=['GET'])
def todays_menus(self, request):
    '''
        Returns a list of menus that were uploaded
        today. The voting candidates!
    '''
    return Response(DetailedMenuSerializer(
        Menu.objects.filter(votable=True),
        many=True
    ).data)


@api_view(http_method_names=['GET', 'POST', 'DELETE'])
def menus(request, restaurant_id: str) -> Response:
    '''
        Handles requests to the restaurants/<slug:restaurant_id>/menus
        Implements GET, POST, and DELETE.
        @TODO: Add support for more methods
    '''
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        # post a new menu
        # print(f"\nPOST DATA\n{request.data}\n")

        # check request body has correct items
        if "meals" not in request.data:
            raise APIException("Request body missing key 'meals'")

        if "drinks" not in request.data:
            raise APIException("Request body missing key 'drinks'")

        # ensure resturant can only past once a day
        if Menu.objects.filter(
            date_created__date=date.today(),
            restaurant=restaurant
        ).exists():
            raise APIException("Menu for today already submitted.")

        # we start by creating the menu
        new_menu = Menu.objects.create(restaurant=restaurant)

        # pop items accordingly and inject type and menu id
        raw_drinks = request.data.pop('drinks')
        raw_meals = request.data.pop('meals')

        for item in raw_drinks:
            item['type'] = 'D'
            item['menu'] = new_menu.id

        for item in raw_meals:
            item['type'] = 'M'
            item['menu'] = new_menu.id

        # create menu items
        # for drink in drinks:
        serialized_menu_items = MenuItemSerializer(
            data=[*raw_drinks, *raw_meals],
            many=True
        )
        serialized_menu_items.is_valid(raise_exception=True)

        # save items
        serialized_menu_items.save()

        return Response(DetailedMenuSerializer(new_menu).data)

    # Handles GET. Returns all menus matching the restaturant
    # with id restaurant_id
    return Response(
        MenuSerializer(
            Menu.objects.filter(restaurant=restaurant_id),
            many=True
        ).data
    )


@api_view(http_method_names=['GET', 'DELETE'])
def menu_detail(
    request,
    restaurant_id,
    menu_id
) -> Response:
    '''
        Handles requests to the restaurants/<slug:restaurant_id>/menus
        Implements GET, POST, and DELETE.
        @TODO: Add support for more methods
    '''
    menu = get_object_or_404(Menu, id=menu_id, restaurant__id=restaurant_id)

    if request.method == 'DELETE':
        menu.delete()
        return Response(status.HTTP_200_OK)

    # returns the menu
    return Response(DetailedMenuSerializer(menu).data)
