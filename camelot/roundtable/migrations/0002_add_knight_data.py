# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.core.management import call_command

class Migration(DataMigration):

    def forwards(self, orm):
        call_command('loaddata', '0002_add_knight_data.json')

    def backwards(self, orm):
        "Write your backwards methods here."

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
