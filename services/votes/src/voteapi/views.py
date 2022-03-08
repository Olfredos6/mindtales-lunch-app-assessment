from voteapi.models import Vote
from voteapi.serializers import VoteSerializer
from rest_framework.viewsets import ModelViewSet
from voteapi.custom_auth import CustomTokenAuth


class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
