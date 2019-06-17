from django.conf.urls import url
from .views.post_reply import PostReplyView, PostReplyDetail
from .views.album_reply import AlbumReplyView, AlbumReplyDetail
from .views.artist_reply import ArtistReplyView, ArtistReplyDetail
from .views.song_reply import SongReplyView, SongReplyDetail

urlpatterns = [

    # Post replies
    url(r'^post_replies$', PostReplyView.as_view()),
    url(r'^post_replies/(?P<post_reply_id>[\d]+)$', PostReplyDetail.as_view()),
    # Post replies
    url(r'^album_replies$', AlbumReplyView.as_view()),
    url(r'^album_replies/(?P<album_reply_id>[\d]+)$', AlbumReplyDetail.as_view()),

    # Post replies
    url(r'^artist_replies$', ArtistReplyView.as_view()),
    url(r'^artist_replies/(?P<artist_reply_id>[\d]+)$', ArtistReplyDetail.as_view()),      

      # Post replies
    url(r'^song_replies$', SongReplyView.as_view()),
    url(r'^song_replies/(?P<song_reply_id>[\d]+)$', SongReplyDetail.as_view()),

]
