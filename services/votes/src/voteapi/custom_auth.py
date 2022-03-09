from rest_framework import exceptions
from rest_framework import authentication
import requests
from os import getenv


class CustomTokenAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            raise exceptions.AuthenticationFailed(
                'No authentication token provided.'
            )

        # validates from auth service
        headers = {"Authorization": token}
        response = requests.get(f"{getenv('AUTH_SERVICE_BASE_URL')}/users", headers=headers)

        if not response.ok:
            raise exceptions.AuthenticationFailed(response.json())

        # inject token in payload in case the view needs it
        user = response.json()
        user['token'] = token

        return (user, None)
