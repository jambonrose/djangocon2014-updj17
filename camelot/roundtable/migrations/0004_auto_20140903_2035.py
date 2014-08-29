# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roundtable', '0003_knight_traitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knight',
            name='traitor',
            field=models.BooleanField(default=False),
        ),
    ]
