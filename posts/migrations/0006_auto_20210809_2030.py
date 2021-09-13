# Generated by Django 3.1.6 on 2021-08-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210723_0534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='bad',
            new_name='dislikes',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='good',
            new_name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
