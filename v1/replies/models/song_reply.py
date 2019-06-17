from django.db import models
from v1.music.models.song import Song
from .reply import Reply


class SongReply(Reply):
    song = models.ForeignKey(Song)

    class Meta:
        default_related_name = 'song_replies'

    def __str__(self):
        return self.body
