from django.db import models

import uuid
from datetime import date


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

    @property
    def votable(self):
        '''
            Specifies if a menu can particpate in a vote.
            Such as menu is one that has been uploaded on the day
            of voting. Returns True if the menu was uploaded today
        '''
        # print("======>", self.date_created.date(), date.today())
        return True if self.date_created.date() == date.today() else False


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
        related_name='items',
        on_delete=models.CASCADE,
        null=False
    )

    # Need to represent the type of the menu item
    # An menu item may be a Meal or a Drink
    type_choices = [('M', 'meal'), ('D', 'drink')]
    type: models.CharField = models.CharField(
        max_length=1,
        choices=type_choices
    )

    name: models.CharField = models.CharField(
        max_length=100,
        null=False
    )

    description: models.CharField = models.CharField(
        max_length=250,
        null=True
    )
