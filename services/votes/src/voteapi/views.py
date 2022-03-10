from datetime import date
import requests as Request
from os import getenv

from voteapi.models import Vote
from voteapi.serializers import VoteSerializer
from voteapi.permissions import IsEmployee

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException


class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsEmployee]

    def create(self, request):
        employee = request.user
        vote = request.data

        # make sure this employee has not voted today yet
        if Vote.objects.filter(
            employee=employee.get('id'),
            menu=vote.get('menu'),
            date_casted__date=date.today()
        ).exists():
            return Response(status.HTTP_400_BAD_REQUEST)

        # make sure the points are correct by making usre the
        # sum is 6.
        keys = [int(k) for k in vote.keys()]
        if sum(keys) != 6 or list(filter(lambda x: x < 0, keys)):
            return Response(status.HTTP_400_BAD_REQUEST)

        # make sure each menu does exist
        response = Request.get(
            getenv('VOTABLE_URL'),
            headers={
                "Authorization": employee.get('token')
            }
        )
        if response.ok is not True:
            raise APIException("Unable to reach restuarants service")

        votables = response.json()
        # make sure all voted menus are included in the list
        # of votable menus
        set_of_votable = set([menu.get('id') for menu in votables])
        set_of_voted = set(vote.values())
        if len(set_of_votable.intersection(set_of_voted)) != 3:
            raise APIException(
                ' \
                All menus must be included in the list of \
                votable menus. See list at /restaurants/votable_menus \
                and be unique.\
                '
            )

        # serialize the vote
        serialized_votes = self.get_serializer(
            data=[{
                'employee': employee.get('id'),
                'point': point,
                'menu': vote.get(point)
            } for point in vote],
            many=True
        )
        serialized_votes.is_valid(raise_exception=True)

        # proceed with saving
        serialized_votes.save()
        # The middleware should route to old method if header
        # has a differnt value than current API

        return Response(status.HTTP_201_CREATED)
