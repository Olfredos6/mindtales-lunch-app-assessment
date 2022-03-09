from rest_framework.viewsets import ModelViewSet
from core.models import Restaurant, Menu
from core.serializers import RestaurantSerializer, MenuSerializer
from core.permissions import IsSuperUser
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
import requests
from rest_framework.response import Response


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsSuperUser]

    @action(methods=["GET", "POST", "UPDATE", "PATCH"], detail=True)
    def manager(self, request, pk):
        '''
            Handles GET, POST, UUPDATE, and PATCH requests to
            /restaurants/:restaurant-pk/manager
            
            Requests are then forwarded to /auth/managers if a restaurant
            object match was found
        '''
        print("User ---->", request.user)
        # get the restaurant object or return 404
        restaurant = get_object_or_404(Restaurant, id=pk)
        
        # init objects
        payload = {'id': restaurant.id}  
        headers = {
            'Authorization': request.user.get("token")
        }

        # if request.method == "GET":
        #     response = requests.get(f"/auth/manager?restaurant={payload.get("id")}")
        
        return Response(RestaurantSerializer(restaurant).data)


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
