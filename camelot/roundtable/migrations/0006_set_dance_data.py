# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def unset_dancing_default(apps, schema_editor):
    Knight = apps.get_model('rtable', 'Knight')
    knights = Knight.objects.filter(name__in=[
        'Bors', 'Ector', 'Robin'])
    for knight in knights:
        knight.dances = False
        knight.save()


def reset_dancing_default(apps, schema_editor):
    Knight = apps.get_model('rtable', 'Knight')
    knights = Knight.objects.filter(name__in=[
        'Bors', 'Ector', 'Robin'])
    for knight in knights:
        knight.dances = True
        knight.save()


class Migration(migrations.Migration):

    dependencies = [
        ('rtable', '0005_knight_dances'),
    ]

    operations = [
        migrations.RunPython(
            unset_dancing_default,
            reverse_code=reset_dancing_default)
    ]
