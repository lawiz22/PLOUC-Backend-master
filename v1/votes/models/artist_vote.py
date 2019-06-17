from django.db import models
from v1.music.models.artist import Artist
from v1.votes.models.vote import Vote


class ArtistVote(Vote):
    artist = models.ForeignKey(Artist)

    class Meta:
        default_related_name = 'artist_votes'
        unique_together = ('artist', 'user')

    def __str__(self):
        return f'artist: {self.artist.id} - value: {self.value}'
