# Generated by Django 3.1.6 on 2021-07-06 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_age'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
