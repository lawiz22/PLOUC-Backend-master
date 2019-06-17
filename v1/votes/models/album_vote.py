from django.db import models
from v1.music.models.album import Album
from v1.votes.models.vote import Vote


class AlbumVote(Vote):
    album = models.ForeignKey(Album)

    class Meta:
        default_related_name = 'album_votes'
        unique_together = ('album', 'user')

    def __str__(self):
        return f'album: {self.album.id} - value: {self.value}'
