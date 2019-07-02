from django.conf import settings
from django.db import models
from datetime import datetime 
from v1.music.models.artist import Artist
from v1.general.created_modified import CreatedModified

class Album(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    artist = models.CharField(max_length=250)
    artist_name = models.ForeignKey( Artist, on_delete=models.CASCADE,default='' )
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField()
    date_action = models.DateTimeField(default=datetime.now, blank=True)
    is_favorite = models.BooleanField(default=False)

    class Meta:
        default_related_name = 'albums'

    def __str__(self):
        return self.album_title + ' - ' + self.artist
