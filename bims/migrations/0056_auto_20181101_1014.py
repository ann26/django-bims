# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-01 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0055_auto_20181101_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
