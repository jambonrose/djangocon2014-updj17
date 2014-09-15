# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtable', '0004_label_lancelot_traitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='knight',
            name='dances',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
