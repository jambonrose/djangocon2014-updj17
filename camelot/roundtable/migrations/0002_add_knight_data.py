# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from django.core.management import call_command


def add_knight_data(apps, schema_editor):
    call_command('loaddata', 'knight_data.json')


def remove_knight_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('roundtable', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_knight_data,
            reverse_code=remove_knight_data),
    ]
