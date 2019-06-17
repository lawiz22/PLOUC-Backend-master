from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.music.models.album import Album
from v1.replies.models.album_reply import AlbumReply
from v1.replies.serializers.album_reply import AlbumReplySerializer
from v1.votes.serializers.album_vote import AlbumVoteSerializer


class AlbumSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    album_reply_count = serializers.SerializerMethodField()
    album_votes = AlbumVoteSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = '__all__'

    @staticmethod
    def get_album_reply_count(album):
        return AlbumReply.objects.filter(album=album).count()

class AlbumSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Album
        fields = '__all__'
   

class AlbumSerializerFull(AlbumSerializer):
    album_replies = AlbumReplySerializer(many=True, read_only=True)

class AlbumSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Album
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit albums from other users')
        return data



