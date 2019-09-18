# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-02 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0013_auto_20180629_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boundary',
            name='code_name',
            field=models.CharField(default=b'EMPTY', max_length=128),
        ),
        migrations.AlterUniqueTogether(
            name='boundary',
            unique_together=set([('name', 'code_name', 'type')]),
        ),
    ]
