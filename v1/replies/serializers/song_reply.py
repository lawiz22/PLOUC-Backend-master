from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.replies.models.song_reply import SongReply


class SongReplySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = SongReply
        fields = '__all__'


class SongReplySerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = SongReply
        fields = '__all__'

    def validate_user(self, user):
        """
        Validate authenticated user
        """

        if user != self.context['request'].user:
            raise serializers.ValidationError('You can not create Song replies for other users')
        return user


class SongReplySerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = SongReply
        exclude = ('post', 'user')

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit Song replies from other users')
        return data
