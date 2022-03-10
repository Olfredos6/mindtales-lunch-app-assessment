from core.models import Restaurant, Menu, MenuItem
from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    votable = serializers.BooleanField()

    class Meta:
        model = Menu
        fields = "__all__"
        read_only_fields = ['date_created']


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = "__all__"

    def to_representation(self, instance):
        '''
            Because we want the type of the item
            to be displayed in full
        '''
        repr = super().to_representation(instance)
        repr['type'] = instance.get_type_display()

        return repr


class DetailedMenuSerializer(serializers.ModelSerializer):
    '''
        Returns a more detailed menu object which
        includes menu items
    '''
    items = MenuItemSerializer(read_only=True, many=True)

    class Meta:
        model = Menu
        fields = "__all__"
        read_only_fields = ['date_created', 'items']
