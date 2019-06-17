from django.contrib import admin
from .models.post_vote import PostVote
from .models.album_vote import AlbumVote
from .models.artist_vote import ArtistVote
from .models.song_vote import SongVote


admin.site.register(PostVote)
admin.site.register(AlbumVote)
admin.site.register(ArtistVote)
admin.site.register(SongVote)
