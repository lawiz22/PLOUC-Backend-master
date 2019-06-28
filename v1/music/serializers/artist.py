from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.music.models.artist import Artist
from v1.music.models.album import Album
from v1.music.models.song import Song
from v1.music.serializers.album import AlbumSerializer
from v1.music.serializers.song import SongSerializer
from v1.replies.models.artist_reply import ArtistReply
from v1.replies.serializers.artist_reply import ArtistReplySerializer
from v1.votes.serializers.artist_vote import ArtistVoteSerializer


class ArtistSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    artist_reply_count = serializers.SerializerMethodField()
    artist_album_count = serializers.SerializerMethodField()
    artist_song_count = serializers.SerializerMethodField()
    artist_votes = ArtistVoteSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = '__all__'

    @staticmethod
    def get_artist_reply_count(artist):
        return ArtistReply.objects.filter(artist=artist).count()
    @staticmethod
    def get_artist_album_count(artist):
        return Album.objects.filter(artist_name=artist).count()
    @staticmethod
    def get_artist_song_count(artist):
        return Song.objects.filter(artist_id=artist).count()    

class ArtistSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Artist
        fields = '__all__'
   

class ArtistSerializerFull(ArtistSerializer):
    artist_replies = ArtistReplySerializer(many=True, read_only=True
    )
    artist_albums = AlbumSerializer(many=True, read_only=True
    )
    artist_songs = SongSerializer(many=True, read_only=True
    )

class ArtistSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Artist
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit artists from other users')
        return data



