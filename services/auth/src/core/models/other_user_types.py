from django.contrib.auth import get_user_model


User = get_user_model()


class Employee(User):  # type: ignore
    '''
        Represetns an employee or staff.
        Different from a RestaturantManager who is
        not considered staff.
    '''
    is_staff = True


class RestaurantManager(User):  # type: ignore
    '''
        Represents a restaturant manager
    '''
    pass
