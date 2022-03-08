from rest_framework import exceptions
from rest_framework import authentication
import requests


class CustomTokenAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            raise exceptions.AuthenticationFailed(
                'No authentication token provided.'
            )

        # validates from auth service
        headers = {"Authorization": token}
        response = requests.get("http://auth:3000/auth/users", headers=headers)

        if not response.ok:
            raise exceptions.AuthenticationFailed(response.json())

        return (response.json(), None)
