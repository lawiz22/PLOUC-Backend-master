from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.votes.models.artist_vote import ArtistVote
from v1.votes.serializers.artist_vote import ArtistVoteSerializer, ArtistVoteSerializerCreate, ArtistVoteSerializerUpdate


# artist_votes
class ArtistVoteView(APIView):

    @staticmethod
    def post(request):
        """
        Create artist vote
        """

        serializer = ArtistVoteSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(ArtistVoteSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# artist_votes/{artist_vote_id}
class ArtistVoteDetail(APIView):

    @staticmethod
    def patch(request, artist_vote_id):
        """
        Update artist vote
        """

        artist_vote = get_object_or_404(ArtistVote, pk=artist_vote_id)
        serializer = ArtistVoteSerializerUpdate(artist_vote, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ArtistVoteSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, artist_vote_id):
        """
        Delete artist vote
        """

        artist_vote = get_object_or_404(ArtistVote, pk=artist_vote_id)
        if artist_vote.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        artist_vote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
