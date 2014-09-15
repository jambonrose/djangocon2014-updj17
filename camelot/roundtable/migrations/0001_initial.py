# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Knight',
            fields=[
                ('id',
                 models.AutoField(
                     primary_key=True,
                     verbose_name='ID',
                     serialize=False,
                     auto_created=True)),
                ('name',
                 models.CharField(
                     max_length=63)),
            ],
            options={},
            bases=(models.Model,),
        ),
    ]
