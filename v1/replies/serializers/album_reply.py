from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.replies.models.album_reply import AlbumReply


class AlbumReplySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AlbumReply
        fields = '__all__'


class AlbumReplySerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = AlbumReply
        fields = '__all__'

    def validate_user(self, user):
        """
        Validate authenticated user
        """

        if user != self.context['request'].user:
            raise serializers.ValidationError('You can not create Album replies for other users')
        return user


class AlbumReplySerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = AlbumReply
        exclude = ('post', 'user')

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit Album replies from other users')
        return data
