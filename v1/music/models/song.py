from django.conf import settings

from django.db import models
from v1.music.models.album import Album
from v1.music.models.artist import Artist
from v1.general.created_modified import CreatedModified



class Song(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default='')
    album = models.ForeignKey( Album, on_delete=models.CASCADE)
    artist_id = models.ForeignKey( Artist, on_delete=models.CASCADE,default='' )
    song_title = models.CharField(max_length=250)
    song_image = models.ImageField(default='')
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    class Meta:
        default_related_name = 'songs'

    def __str__(self):
        return self.song_title        
