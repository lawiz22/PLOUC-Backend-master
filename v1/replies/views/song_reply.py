from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.replies.models.song_reply import SongReply
from v1.replies.serializers.song_reply import SongReplySerializer, SongReplySerializerCreate, SongReplySerializerUpdate


# Song_replies
class SongReplyView(APIView):

    @staticmethod
    def post(request):
        """
        Create Song reply
        """

        serializer = SongReplySerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(SongReplySerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# post_replies/{song_reply_id}
class SongReplyDetail(APIView):

    @staticmethod
    def patch(request, song_reply_id):
        """
        Update song reply
        """

        song_reply = get_object_or_404(SongReply, pk=song_reply_id)
        serializer = SongReplySerializerUpdate(song_reply, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(SongReplySerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, song_reply_id):
        """
        Delete song reply
        """

        song_reply = get_object_or_404(SongReply, pk=song_reply_id)
        if song_reply.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        song_reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
