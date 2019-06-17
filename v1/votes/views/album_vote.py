from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.votes.models.album_vote import AlbumVote
from v1.votes.serializers.album_vote import AlbumVoteSerializer, AlbumVoteSerializerCreate, AlbumVoteSerializerUpdate

# album_votes
class AlbumVoteView(APIView):

    @staticmethod
    def post(request):
        """
        Create album vote
        """

        serializer = AlbumVoteSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(AlbumVoteSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# album_votes/{album_vote_id}
class AlbumVoteDetail(APIView):

    @staticmethod
    def patch(request, album_vote_id):
        """
        Update album vote
        """

        album_vote = get_object_or_404(AlbumVote, pk=album_vote_id)
        serializer = AlbumVoteSerializerUpdate(album_vote, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(AlbumVoteSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, album_vote_id):
        """
        Delete album vote
        """

        album_vote = get_object_or_404(AlbumVote, pk=album_vote_id)
        if album_vote.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        album_vote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
