# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Knight'
        db.create_table(
            'roundtable_knight',
            (('id',
              self.gf(
                  'django.db.models.fields.AutoField')(
                      primary_key=True)),
             ('name',
              self.gf(
                  'django.db.models.fields.CharField')(
                      max_length=63)),
             ))
        db.send_create_signal('roundtable', ['Knight'])

    def backwards(self, orm):
        # Deleting model 'Knight'
        db.delete_table('roundtable_knight')

    models = {
        'roundtable.knight': {
            'Meta': {'object_name': 'Knight'},
            'id': ('django.db.models.fields.AutoField',
                   [],
                   {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField',
                     [],
                     {'max_length': '63'})}}

    complete_apps = ['roundtable']
