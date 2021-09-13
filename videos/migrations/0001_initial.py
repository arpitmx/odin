# Generated by Django 3.1.6 on 2021-07-20 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('video_file', models.FileField(upload_to='')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('licence', models.CharField(max_length=1)),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('playlist', models.ForeignKey(blank=True, default='playlists', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='videos', to='features.playlist')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
    ]
