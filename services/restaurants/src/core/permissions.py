from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    '''
        Permission that only grant total access to
        the superuser. Ohters only get SAFE_METHODS
        access
    '''
    message = "Superuser accesss required to permform this operation"

    def has_permission(self, request, view):
        if request.user.get("is_superuser") is True:
            return True
        return request.method in permissions.SAFE_METHODS


class IsManager(permissions.BasePermission):
    '''
        Permission that only grant total access to
        a manager. Ohters only get SAFE_METHODS
        access
    '''
    message = "Manager accesss required to permform this operation"

    def has_permission(self, request, view):
        if request.user.get("is_manager") is True:
            return True
        return request.method in permissions.SAFE_METHODS
