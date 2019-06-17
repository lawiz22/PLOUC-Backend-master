from django.conf.urls import url
from .views.post_vote import PostVoteView, PostVoteDetail
from .views.album_vote import AlbumVoteView, AlbumVoteDetail
from .views.artist_vote import ArtistVoteView, ArtistVoteDetail
from .views.song_vote import SongVoteView, SongVoteDetail


urlpatterns = [

    # Post votes
    url(r'^post_votes$', PostVoteView.as_view()),
    url(r'^post_votes/(?P<post_vote_id>[\d]+)$', PostVoteDetail.as_view()),

     # Albums votes
    url(r'^album_votes$', AlbumVoteView.as_view()),
    url(r'^album_votes/(?P<album_vote_id>[\d]+)$', AlbumVoteDetail.as_view()),

    # Artists votes
    url(r'^artist_votes$', ArtistVoteView.as_view()),
    url(r'^artist_votes/(?P<artist_vote_id>[\d]+)$', ArtistVoteDetail.as_view()),        

     # Songs votes
    url(r'^song_votes$', SongVoteView.as_view()),
    url(r'^song_votes/(?P<song_vote_id>[\d]+)$', SongVoteDetail.as_view()),

]
