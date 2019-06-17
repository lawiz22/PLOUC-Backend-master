from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.votes.models.song_vote import SongVote
from v1.votes.serializers.song_vote import SongVoteSerializer, SongVoteSerializerCreate, SongVoteSerializerUpdate

# song_votes
class SongVoteView(APIView):

    @staticmethod
    def post(request):
        """
        Create song vote
        """

        serializer = SongVoteSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(SongVoteSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# song_votes/{song_vote_id}
class SongVoteDetail(APIView):

    @staticmethod
    def patch(request, song_vote_id):
        """
        Update song vote
        """

        song_vote = get_object_or_404(SongVote, pk=song_vote_id)
        serializer = SongVoteSerializerUpdate(song_vote, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(SongVoteSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, song_vote_id):
        """
        Delete song vote
        """

        song_vote = get_object_or_404(SongVote, pk=song_vote_id)
        if song_vote.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        song_vote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
