from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Employee(User):  # type: ignore
    '''
        Represetns an employee or staff.
        Different from a RestaturantManager who is
        not considered staff.
    '''
    is_staff: models.BooleanField = models.BooleanField(
        _("staff status"),
        default=True,
        help_text=_("Designates whether the user is an employee"),
    )


class RestaurantManager(User):  # type: ignore
    '''
        Represents a restaturant manager
    '''
    pass
