# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def set_lancelot_traitor(apps, schema_editor):
    Knight = apps.get_model('rtable', 'Knight')
    lancelot = Knight.objects.get(
        name__iexact='Lancelot')
    lancelot.traitor = True
    lancelot.save()

def unset_lancelot_traitor(apps, schema_editor):
    Knight = apps.get_model('rtable', 'Knight')
    lancelot = Knight.objects.get(
        name__iexact='Lancelot')
    lancelot.traitor = False
    lancelot.save()

class Migration(migrations.Migration):

    dependencies = [
        ('rtable', '0003_knight_traitor'),
    ]

    operations = [
            migrations.RunPython(
                set_lancelot_traitor,
                reverse_code=unset_lancelot_traitor)
    ]
