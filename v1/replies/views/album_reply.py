from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.replies.models.album_reply import AlbumReply
from v1.replies.serializers.album_reply import AlbumReplySerializer, AlbumReplySerializerCreate, AlbumReplySerializerUpdate


# Album_replies
class AlbumReplyView(APIView):

    @staticmethod
    def post(request):
        """
        Create Album reply
        """

        serializer = AlbumReplySerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(AlbumReplySerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# post_replies/{album_reply_id}
class AlbumReplyDetail(APIView):

    @staticmethod
    def patch(request, album_reply_id):
        """
        Update album reply
        """

        album_reply = get_object_or_404(AlbumReply, pk=album_reply_id)
        serializer = AlbumReplySerializerUpdate(album_reply, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(AlbumReplySerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, album_reply_id):
        """
        Delete album reply
        """

        album_reply = get_object_or_404(AlbumReply, pk=album_reply_id)
        if album_reply.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        album_reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
