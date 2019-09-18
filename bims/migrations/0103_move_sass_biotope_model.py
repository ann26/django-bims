# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-11 07:36
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models


def update_contentypes(apps, schema_editor):
    """
    Updates content types.
    We want to have the same content type id, when the model is moved and renamed.
    """
    ContentType = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias

    # Move the ModelThatShouldBeMoved model to app2 and rename to ModelThatWasMoved
    qs = ContentType.objects.using(db_alias).filter(app_label='sass', model='sassbiotope')
    qs.update(app_label='bims', model='sassbiotope')


def update_contentypes_reverse(apps, schema_editor):
    """
    Reverts changes in content types.
    """
    ContentType = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias

    # Move the ModelThatWasMoved model to app1 and rename to ModelThatShouldBeMoved
    qs = ContentType.objects.using(db_alias).filter(app_label='bims', model='sassbiotope')
    qs.update(app_label='sass', model='sassbiotope')



class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0102_merge_20190111_0728'),
        ('sass', '0014_auto_20190111_0809'),
        ('contenttypes', '0001_initial'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='SassBiotope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('additional_data',
                 django.contrib.postgres.fields.jsonb.JSONField(blank=True,
                                                                default={},
                                                                encoder=django.core.serializers.json.DjangoJSONEncoder,
                                                                null=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('display_order', models.FloatField(blank=True, null=True)),
                ('biotope_form', models.CharField(blank=True,
                                                  choices=[(b'0', b'0'),
                                                           (b'1', b'1'),
                                                           (b'2', b'2')],
                                                  max_length=2)),
            ],
            options={
                'db_table': 'bims_sassbiotope',
            },
            bases=(models.Model,),
        ),
    ]

    database_operations = [
        migrations.RunPython(update_contentypes, update_contentypes_reverse),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=state_operations,
            database_operations=database_operations
        ),
    ]
