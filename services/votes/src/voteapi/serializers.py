from voteapi.models import Vote
from rest_framework.serializers import ModelSerializer


class VoteSerializer(ModelSerializer):

    class Meta:
        model = Vote
        fields = '__all__'
