from django.db import models
from v1.music.models.artist import Artist
from .reply import Reply


class ArtistReply(Reply):
    artist = models.ForeignKey(Artist)

    class Meta:
        default_related_name = 'artist_replies'

    def __str__(self):
        return self.body
