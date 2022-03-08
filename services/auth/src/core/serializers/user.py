from rest_framework import serializers
from core.models import Employee, RestaurantManager
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class RestaurantManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantManager
        fields = '__all__'
