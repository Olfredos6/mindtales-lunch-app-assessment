from rest_framework import serializers
from core.models import Employee, RestaurantManager


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class RestaurantManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantManager
        fields = '__all__'
