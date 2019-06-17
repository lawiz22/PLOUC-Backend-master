from rest_framework import serializers
from v1.votes.models.album_vote import AlbumVote


class AlbumVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlbumVote
        fields = '__all__'


class AlbumVoteSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AlbumVote
        fields = '__all__'


class AlbumVoteSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = AlbumVote
        exclude = ('album', 'user')

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit album votes from other users')
        return data
