from django.conf import settings
from django.db import models
from datetime import datetime  
from v1.general.created_modified import CreatedModified

class Artist(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default='')
    artist = models.CharField(max_length=250)
    artist_image = models.ImageField(default='')
    is_favorite = models.BooleanField(default=False)
    artist_desc = models.CharField(max_length=250,default='')
    date_debut = models.DateTimeField(default=datetime.now, blank=True)
    date_fin = models.DateTimeField(default=datetime.now, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        default_related_name = 'artist'

    def __str__(self):
        return self.artist
