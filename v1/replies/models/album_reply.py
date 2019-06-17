from django.db import models
from v1.music.models.album import Album
from .reply import Reply


class AlbumReply(Reply):
    album = models.ForeignKey(Album)

    class Meta:
        default_related_name = 'album_replies'

    def __str__(self):
        return self.body
