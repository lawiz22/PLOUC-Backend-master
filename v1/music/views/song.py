from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import (
   LimitOffsetPagination,
   PageNumberPagination,
)
from v1.filters.songs.song import song_filter
from v1.music.models.song import Song
from v1.music.serializers.song import SongSerializer, SongSerializerCreate, SongSerializerFull, SongSerializerUpdate




# songs
class SongView(APIView):

    
    @staticmethod
    def get(request):
        """
        List songs
        """
        

        songs = Song.objects.all().order_by('id')
        songs = song_filter(request, songs)
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(songs, request)

        if type(songs) == Response:
            return songs
        return Response(SongSerializer(result_page, many=True).data)

    @staticmethod
    def post(request):
        """
        Create song
        """

        serializer = SongSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(SongSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      


# songs/{song_id}
class SongDetail(APIView):

    @staticmethod
    def get(request, song_id):
        """
        View individual song
        """

        song = get_object_or_404(Song, pk=song_id)
        return Response(SongSerializerFull(song).data)

    @staticmethod
    def patch(request, song_id):
        """
        Update song
        """

        song = get_object_or_404(Song, pk=song_id)
        serializer = SongSerializerUpdate(song, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(SongSerializerFull(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, song_id):
        """
        Delete song
        """

        song = get_object_or_404(Song, pk=song_id)
        if song.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
