# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roundtable', '0002_add_knight_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='knight',
            name='traitor',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
