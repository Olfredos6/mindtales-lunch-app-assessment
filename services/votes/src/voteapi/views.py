from voteapi.models import Vote
from voteapi.serializers import VoteSerializer
from rest_framework.viewsets import ModelViewSet


class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
