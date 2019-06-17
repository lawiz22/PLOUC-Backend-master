from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.replies.models.artist_reply import ArtistReply
from v1.replies.serializers.artist_reply import ArtistReplySerializer, ArtistReplySerializerCreate, ArtistReplySerializerUpdate


# Artist_replies
class ArtistReplyView(APIView):

    @staticmethod
    def post(request):
        """
        Create Artist reply
        """

        serializer = ArtistReplySerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(ArtistReplySerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# post_replies/{artist_reply_id}
class ArtistReplyDetail(APIView):

    @staticmethod
    def patch(request, artist_reply_id):
        """
        Update artist reply
        """

        artist_reply = get_object_or_404(ArtistReply, pk=artist_reply_id)
        serializer = ArtistReplySerializerUpdate(artist_reply, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ArtistReplySerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, artist_reply_id):
        """
        Delete artist reply
        """

        artist_reply = get_object_or_404(ArtistReply, pk=artist_reply_id)
        if artist_reply.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        artist_reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
