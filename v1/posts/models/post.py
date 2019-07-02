from django.conf import settings
from django.db import models
from datetime import datetime 
from v1.general.created_modified import CreatedModified


class Post(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(blank=True)
    date_debut = models.DateTimeField(default=datetime.now, blank=True)
    date_fin = models.DateTimeField(default=datetime.now, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.title
