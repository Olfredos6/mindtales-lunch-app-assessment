from rest_framework.permissions import BasePermission


class IsEmployee(BasePermission):
    ''' Only allows acces to an employeee '''

    message = "Employee permission required to perfrom this action"

    def has_permission(self, request, view):
        '''
            The authenticated user should
            return true for is_staff
        '''
        return request.user.get('is_staff')
