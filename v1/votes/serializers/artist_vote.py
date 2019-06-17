from rest_framework import serializers
from v1.votes.models.artist_vote import ArtistVote


class ArtistVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtistVote
        fields = '__all__'


class ArtistVoteSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ArtistVote
        fields = '__all__'


class ArtistVoteSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = ArtistVote
        exclude = ('artist', 'user')

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit artist votes from other users')
        return data
