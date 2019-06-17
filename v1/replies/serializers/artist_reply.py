from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.replies.models.artist_reply import ArtistReply


class ArtistReplySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ArtistReply
        fields = '__all__'


class ArtistReplySerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = ArtistReply
        fields = '__all__'

    def validate_user(self, user):
        """
        Validate authenticated user
        """

        if user != self.context['request'].user:
            raise serializers.ValidationError('You can not create Artist replies for other users')
        return user


class ArtistReplySerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = ArtistReply
        exclude = ('post', 'user')

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit Artist replies from other users')
        return data
