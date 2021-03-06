# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-16 23:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_replies', to='music.Album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_replies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'album_replies',
            },
        ),
        migrations.CreateModel(
            name='ArtistReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_replies', to='music.Artist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_replies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'artist_replies',
            },
        ),
        migrations.CreateModel(
            name='PostReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_replies', to='posts.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_replies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'post_replies',
            },
        ),
        migrations.CreateModel(
            name='SongReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_replies', to='music.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_replies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'song_replies',
            },
        ),
    ]
