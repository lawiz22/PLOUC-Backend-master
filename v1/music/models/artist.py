from django.conf import settings
from django.db import models
from v1.general.created_modified import CreatedModified

class Artist(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default='')
    artist = models.CharField(max_length=250)
    artist_image = models.ImageField(default='')
    is_favorite = models.BooleanField(default=False)

    class Meta:
        default_related_name = 'artist'

    def __str__(self):
        return self.artist
