from django.contrib import admin
from .models.post_reply import PostReply
from .models.album_reply import AlbumReply
from .models.artist_reply import ArtistReply
from .models.song_reply import SongReply


admin.site.register(PostReply)
admin.site.register(AlbumReply)
admin.site.register(SongReply)
admin.site.register(ArtistReply)

