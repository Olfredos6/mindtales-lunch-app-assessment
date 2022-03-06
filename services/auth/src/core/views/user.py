from rest_framework import viewsets
from core.models import Employee, RestaurantManager
from core.serializers.user import EmployeeSerializer, \
    RestaurantManagerSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class RestaurantManagerViewSet(viewsets.ModelViewSet):
    queryset = RestaurantManager.objects.all()
    serializer_class = RestaurantManagerSerializer
