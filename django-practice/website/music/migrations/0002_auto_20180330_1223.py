# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='Song_title',
            new_name='song_title',
        ),
        migrations.AddField(
            model_name='song',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
