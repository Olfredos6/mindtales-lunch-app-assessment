from datetime import date
import requests
from os import getenv

from voteapi.models import Vote
from voteapi.serializers import VoteSerializer
from voteapi.permissions import IsEmployee

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.decorators import action


class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsEmployee]

    def return_not_implemented(self, request):
        return Response(status.HTTP_501_NOT_IMPLEMENTED)

    def update(self, request):
        return self.return_not_implemented(request)

    def retrieve(self, request):
        return self.return_not_implemented(request)

    def menus_are_votable(self, employee: dict, menus: list = []) -> None:
        '''
            Used to verify that all supplied menus
            are available for voting. If all is well, execution
            will carry on. Otherwise, an APIException exception
            is raised
        '''
        response = requests.get(
            getenv('VOTABLE_URL', ''),
            headers={
                "Authorization": employee.get('token', '')
            }
        )
        if response.ok is not True:
            raise APIException("Unable to reach restuarants service")

        votables = response.json()
        # make sure all voted menus are included in the list
        # of votable menus
        set_of_votable = set([menu.get('id') for menu in votables])
        set_of_voted = set(menus)

        if len(set_of_votable.intersection(set_of_voted)) != len(menus):
            raise APIException(
                ' \
                All menus must be included in the list of \
                votable menus. See list at /restaurants/votable_menus \
                and be unique.\
                '
            )

    def create(self, request):
        employee = request.user
        vote = request.data

        # make sure this employee has not voted today yet
        if Vote.objects.filter(
            employee=employee.get('id'),
            date_casted__date=date.today()
        ).count() == 3:
            raise APIException(
                f"Employee {employee.get('username')} has already voted"
            )

        # make sure the points are correct by making sure the
        # sum is 6.
        try:
            keys = [int(k) for k in vote.keys()]
            if sum(keys) != 6 or list(filter(lambda x: x < 0, keys)):
                return Response(status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise APIException(e)

        # make sure each menu does exist
        self.menus_are_votable(employee, vote.values())

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

    @action(methods=['GET'], detail=True)
    def old_voting_view(self, request, pk):
        '''
            Old way of voting, one menu per day
            per employee.
        '''
        employee = request.user
        vote = request.data

        # make sure this employee has not voted today yet
        if Vote.objects.filter(
            employee=employee.get('id'),
            date_casted__date=date.today()
        ).count() == 1:
            raise APIException(
                f"Employee {employee.get('username')} has already voted"
            )

        # serialize
        serialized_vote = VoteSerializer(
            data={
                'employee': employee.get('id'),
                'menu': pk,
                'point': 3
            })

        serialized_vote.is_valid(raise_exception=True)

        # ensure menu is among votable
        self.menus_are_votable(employee, vote.values())

        serialized_vote.save()

        return Response(status.HTTP_201_CREATED)

    @action(methods=['GET'], detail=False)
    def results(self, request):
        '''
            Returns voting results for the day
        '''
        from django.db.models import Sum

        vote_results = \
            Vote.objects.filter(date_casted__date=date.today())\
            .values('menu')\
            .annotate(total_points=Sum('point'))\
            .order_by('-total_points')[:3]\


        data = {}
        count = 1
        for item in vote_results:
            data[count] = {
                'menu': item.get('menu'),
                'points': item.get('total_points')
            }
            count += 1
        return Response(data)
