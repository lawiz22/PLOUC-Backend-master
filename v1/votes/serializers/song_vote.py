from rest_framework import serializers
from v1.votes.models.song_vote import SongVote


class SongVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongVote
        fields = '__all__'


class SongVoteSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SongVote
        fields = '__all__'


class SongVoteSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = SongVote
        exclude = ('song', 'user')

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit song votes from other users')
        return data
