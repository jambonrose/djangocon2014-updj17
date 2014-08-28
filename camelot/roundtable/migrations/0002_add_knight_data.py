# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        orm.Knight.objects.bulk_create([
            orm.Knight(name='Bedevere'),
            orm.Knight(name='Bors'),
            orm.Knight(name='Ector'),
            orm.Knight(name='Galahad'),
            orm.Knight(name='Gawain'),
            orm.Knight(name='Lancelot'),
            orm.Knight(name='Robin'),
        ])

    def backwards(self, orm):
        orm.Knight.objects.all().delete()

    models = {
        u'roundtable.knight': {
            'Meta': {'object_name': 'Knight'},
            u'id': (
                'django.db.models.fields.AutoField',
                [],
                {'primary_key': 'True'}),
            'name': (
                'django.db.models.fields.CharField',
                [],
                {'max_length': '63'})
        }
    }

    complete_apps = ['roundtable']
    symmetrical = True
