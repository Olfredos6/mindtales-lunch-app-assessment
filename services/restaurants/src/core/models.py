from django.db import models
import uuid


class Restaurant(models.Model):
    date_created: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name: models.CharField = models.CharField(max_length=150)
    manager: models.IntegerField = models.IntegerField(null=False)


class Menu(models.Model):
    # The date_created field below also represents the date of the menu
    date_created: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    restaurant: models.ForeignKey = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant'
    )


class MenuItem(models.Model):
    '''
        Represents an item meal or drink
        belonging to a menu
    '''
    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    menu: models.ForeignKey = models.ForeignKey(
        Menu,
        related_name='menu_item',
        on_delete=models.CASCADE,
        null=False
    )
    title: models.CharField = models.CharField(
        max_length=100,
        null=False
    )
    description: models.CharField = models.CharField(
        max_length=250,
        null=False
    )
