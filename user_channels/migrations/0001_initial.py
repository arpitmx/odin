# Generated by Django 3.1.6 on 2021-07-24 06:16

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
                ('channel_photo', models.ImageField(default='{{ user.photo }}', upload_to='channel_photo')),
                ('CHANNEL_TYPE', models.CharField(choices=[('A', 'Article'), ('S', 'Audio'), ('V', 'Video')], max_length=1)),
                ('subscribers', models.BigIntegerField(default=0)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
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
