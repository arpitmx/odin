# Generated by Django 3.2.7 on 2021-09-13 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=50)),
                ('channel_photo', models.ImageField(upload_to='channel_photo')),
                ('channel_cover_photo', models.ImageField(default=None, upload_to='channel_cover_photo')),
                ('CHANNEL_TYPE', models.CharField(choices=[('A', 'Article'), ('S', 'Audio'), ('V', 'Video')], max_length=1)),
                ('subscribers', models.BigIntegerField(default=0)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(max_length=50)),
                ('channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='user_channels.channel')),
            ],
            options={
                'verbose_name': 'Playlist',
                'verbose_name_plural': 'Playlists',
            },
        ),
    ]
