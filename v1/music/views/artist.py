from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.filters.artists.artist import artist_filter
from v1.music.models.artist import Artist
from v1.music.serializers.artist import ArtistSerializer, ArtistSerializerCreate, ArtistSerializerFull, ArtistSerializerUpdate


# artists
class ArtistView(APIView):

    @staticmethod
    def get(request):
        """
        List artists
        """

        artists = Artist.objects.all()
        artists = artist_filter(request, artists)
        if type(artists) == Response:
            return artists
        return Response(ArtistSerializer(artists, many=True).data)

    @staticmethod
    def post(request):
        """
        Create artist
        """

        serializer = ArtistSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(ArtistSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# artists/{artist_id}
class ArtistDetail(APIView):

    @staticmethod
    def get(request, artist_id):
        """
        View individual artist
        """

        artist = get_object_or_404(Artist, pk=artist_id)
        return Response(ArtistSerializerFull(artist).data)

    @staticmethod
    def patch(request, artist_id):
        """
        Update artist
        """

        artist = get_object_or_404(Artist, pk=artist_id)
        serializer = ArtistSerializerUpdate(artist, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ArtistSerializerFull(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, artist_id):
        """
        Delete artist
        """

        artist = get_object_or_404(Artist, pk=artist_id)
        if artist.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
