from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    '''
        Permission that only grant total access to
        the superuser. Ohters only get SAFE_METHODS
        access
    '''
    message = "Superuser accesss required to permform this operation"

    def has_permission(self, request, view):
        if request.user.get("is_superuser") == True:
            return True
        return request.method in permissions.SAFE_METHODS