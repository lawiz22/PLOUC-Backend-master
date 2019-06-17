from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.filters.albums.album import album_filter
from v1.music.models.album import Album
from v1.music.serializers.album import AlbumSerializer, AlbumSerializerCreate, AlbumSerializerFull, AlbumSerializerUpdate


# albums
class AlbumView(APIView):

    @staticmethod
    def get(request):
        """
        List albums
        """

        albums = Album.objects.all()
        albums = album_filter(request, albums)
        if type(albums) == Response:
            return albums
        return Response(AlbumSerializer(albums, many=True).data)

    @staticmethod
    def post(request):
        """
        Create album
        """

        serializer = AlbumSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(AlbumSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# albums/{album_id}
class AlbumDetail(APIView):

    @staticmethod
    def get(request, album_id):
        """
        View individual album
        """

        album = get_object_or_404(Album, pk=album_id)
        return Response(AlbumSerializerFull(album).data)

    @staticmethod
    def patch(request, album_id):
        """
        Update album
        """

        album = get_object_or_404(Album, pk=album_id)
        serializer = AlbumSerializerUpdate(album, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(AlbumSerializerFull(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, album_id):
        """
        Delete album
        """

        album = get_object_or_404(Album, pk=album_id)
        if album.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
