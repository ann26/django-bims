# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-29 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0109_auto_20190128_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchprocess',
            name='search_raw_query',
            field=models.TextField(blank=True, null=True),
        ),
    ]