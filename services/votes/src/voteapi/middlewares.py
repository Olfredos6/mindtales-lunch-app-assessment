'''
    The purtpose of this middleware is
    to read the value of the build number
    from the received request an route the
    request through to the correct API end-
    point.

    The header key to read is configured in
    the global-django.env file using the
    API_HEADER_KEY_NAME key. The maximum build
    number using the API's old version is set
    in the environment key named OLD_API_MAX_BUILD
    from the same file
'''
from os import getenv

# from django.urls import reverse
from django.shortcuts import redirect
from django.urls import reverse


class VersionControlMiddleware:

    # def middleware(request):
    #     # this middleware only mingles with the request
    #     # when a voting request is made.
    #     print(request.path, reverse('vote-list'))
    #     if request.method == 'POST' and request.path == reverse('vote-list'):
    #         old_api_latest_build_version = int(getenv('OLD_API_MAX_BUILD'))
    #         client_build_number = int(
    #             request.META.get(
    #                 'HTTP_' + getenv('API_HEADER_KEY_NAME'),
    #                 old_api_latest_build_version + 1
    #                 # deafults to max_build + 1
    #                 # to use latest version of API
    #             )
    #         )

    #         # redirect to view for old version if less or equal
    #         # to max build version
    #         # import json
    #         # data = json.loads(request.body.decode())
    #         # print(data)
    #         if client_build_number <= old_api_latest_build_version:
    #             # request.method = 'POST'
    #             redirect(reverse('old-vote-list'))
    #             # request.path = reverse('vote-old-voting-view')
    #     print(request.path, request.method)
    #     response = get_response(request)

    #     return response

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and request.path == reverse('vote-list'):
            old_api_latest_build_version = int(getenv('OLD_API_MAX_BUILD'))
            client_build_number = int(
                request.META.get(
                    'HTTP_' + getenv('API_HEADER_KEY_NAME'),
                    old_api_latest_build_version + 1
                    # deafults to max_build + 1
                    # to use latest version of API
                )
            )            

            # redirect to view for old version if less or equal
            # to max build version

            if client_build_number <= old_api_latest_build_version:
                import json
                data = json.loads(request.body.decode())
                return redirect(reverse('vote-old-voting-view', kwargs={'pk': data.get('menu')}))

        return self.get_response(request)

    # return middleware
