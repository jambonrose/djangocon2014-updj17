# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


def add_knight_data(apps, schema_editor):
    Knight = apps.get_model('roundtable', 'Knight')
    Knight.objects.bulk_create([
        Knight(name='Arthur'),
        Knight(name='Bedevere'),
        Knight(name='Bors'),
        Knight(name='Ector'),
        Knight(name='Galahad'),
        Knight(name='Gawain'),
        Knight(name='Lancelot'),
        Knight(name='Robin'),
    ])


def remove_knight_data(apps, schema_editor):
    Knight = apps.get_model('roundtable', 'Knight')
    Knight.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('roundtable', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_knight_data,
            reverse_code=remove_knight_data),
    ]
