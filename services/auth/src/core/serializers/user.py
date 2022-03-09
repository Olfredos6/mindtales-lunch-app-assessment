from rest_framework import serializers
from core.models import Employee, RestaurantManager
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']


class OtherUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        Model = self.Meta.model
        password = validated_data.get("password")

        instance = Model(**validated_data)

        instance.set_password(password)
        instance.save()

        return instance


class EmployeeSerializer(OtherUserSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class RestaurantManagerSerializer(OtherUserSerializer):

    class Meta:
        model = RestaurantManager
        fields = '__all__'
