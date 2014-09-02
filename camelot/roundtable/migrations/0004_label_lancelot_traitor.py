# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def set_lancelot_traitor(apps, schema_editor):
    pass

def unset_lancelot_traitor(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('roundtable', '0003_knight_traitor'),
    ]

    operations = [
            migrations.RunPython(
                set_lancelot_traitor,
                reverse_code=unset_lancelot_traitor)
    ]
