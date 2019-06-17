from django.contrib import admin
from .models.album import Album
from .models.artist import Artist
from .models.song import Song


admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Artist)

