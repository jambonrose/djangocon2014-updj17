# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Knight.traitor'
        db.add_column(u'roundtable_knight', 'traitor',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Knight.traitor'
        db.delete_column(u'roundtable_knight', 'traitor')


    models = {
        u'roundtable.knight': {
            'Meta': {'object_name': 'Knight'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'traitor': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['roundtable']