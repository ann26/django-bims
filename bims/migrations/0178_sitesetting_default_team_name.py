# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-17 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0177_auto_20190913_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='default_team_name',
            field=models.CharField(blank=True, help_text=b'Default team name', max_length=150, null=True),
        ),
    ]
