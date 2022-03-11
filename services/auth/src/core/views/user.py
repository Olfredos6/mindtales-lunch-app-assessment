from rest_framework.response import Response
from rest_framework import viewsets
from core.models import Employee, RestaurantManager
from core.serializers.user import EmployeeSerializer, \
    RestaurantManagerSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from core.permissions import IsSuperUser


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_class = [IsAdminUser]

    def create(self, request):
        ''' Overridden because we must ensure
            is_staff is marked as True
        '''
        data = {**request.data, 'is_staff': True}
        staff_serialized = self.get_serializer(data=data)

        # validate data
        staff_serialized.is_valid(raise_exception=True)

        # all is good, let's save
        staff_serialized.save()

        return Response(staff_serialized.data)


class RestaurantManagerViewSet(viewsets.ModelViewSet):
    queryset = RestaurantManager.objects.all()
    serializer_class = RestaurantManagerSerializer
    permission_classes = [IsSuperUser, IsAuthenticated]


@api_view(http_method_names=['GET'])
def users(request):
    ''' Used by other services to collect a specific
        user's profile as employee or restaurant manager
    '''
    user = request.user
    if user.is_superuser:
        return Response(UserSerializer(user).data)

    user_rm = RestaurantManager.objects.filter(user_ptr_id=user.id)
    user_e = Employee.objects.filter(user_ptr_id=user.id)
    if user_rm.exists():
        return Response(RestaurantManagerSerializer(user_rm[0]).data)

    return Response(EmployeeSerializer(user_e[0]).data)
