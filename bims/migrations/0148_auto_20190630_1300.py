# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-30 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0147_auto_20190625_0257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('get_all_email', 'Get all email'),)},
        ),
    ]