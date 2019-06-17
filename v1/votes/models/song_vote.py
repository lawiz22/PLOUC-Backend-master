from django.db import models
from v1.music.models.song import Song
from v1.votes.models.vote import Vote


class SongVote(Vote):
    song = models.ForeignKey(Song)

    class Meta:
        default_related_name = 'song_votes'
        unique_together = ('song', 'user')

    def __str__(self):
        return f'song: {self.song.id} - value: {self.value}'
