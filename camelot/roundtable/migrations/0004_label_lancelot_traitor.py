# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        lancelot = orm.Knight.objects.get(
            name__iexact="Lancelot")
        lancelot.traitor = True
        lancelot.save()

    def backwards(self, orm):
        lancelot = orm.Knight.objects.get(
            name__iexact="Lancelot")
        lancelot.traitor = False
        lancelot.save()

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
                {'max_length': '63'}),
            'traitor': (
                'django.db.models.fields.BooleanField',
                [],
                {})
        }
    }

    complete_apps = ['roundtable']
    symmetrical = True
