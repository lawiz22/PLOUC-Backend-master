from django.conf.urls import url
from .views.album import AlbumView, AlbumDetail
from .views.artist import ArtistView, ArtistDetail
from .views.song import SongView, SongDetail


urlpatterns = [

    # Posts
    
    # url(r'^album$', AlbumView.as_view()),
    url(r'^song$', SongView.as_view()),


    url(r'^albums$', AlbumView.as_view()),
    url(r'^albums/(?P<album_id>[\d]+)$', AlbumDetail.as_view()),

    url(r'^artists$', ArtistView.as_view()),
    url(r'^artists/(?P<artist_id>[\d]+)$', ArtistDetail.as_view()),        


    url(r'^songs$', SongView.as_view()),
    url(r'^songs/(?P<song_id>[\d]+)$', SongDetail.as_view()),
   
   

]
