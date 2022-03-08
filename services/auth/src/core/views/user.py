from rest_framework.response import Response
from rest_framework import viewsets
from core.models import Employee, RestaurantManager
from core.serializers.user import EmployeeSerializer, \
    RestaurantManagerSerializer, UserSerializer
from rest_framework.decorators import api_view


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class RestaurantManagerViewSet(viewsets.ModelViewSet):
    queryset = RestaurantManager.objects.all()
    serializer_class = RestaurantManagerSerializer


@api_view(http_method_names=['GET'])
def users(request):
    return Response(UserSerializer(request.user).data)
