from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.music.models.song import Song
from v1.replies.models.song_reply import SongReply
from v1.replies.serializers.song_reply import SongReplySerializer
from v1.votes.serializers.song_vote import SongVoteSerializer


class SongSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    song_reply_count = serializers.SerializerMethodField()
    song_votes = SongVoteSerializer(many=True, read_only=True)
    class Meta:
        model = Song
        fields = '__all__'

    @staticmethod
    def get_song_reply_count(song):
        return SongReply.objects.filter(song=song).count()

class SongSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Song
        fields = '__all__'
   

class SongSerializerFull(SongSerializer):
    song_replies = SongReplySerializer(many=True, read_only=True)

class SongSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Song
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit songs from other users')
        return data



