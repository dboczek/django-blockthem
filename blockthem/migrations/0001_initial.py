# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Rule'
        db.create_table('blockthem_rule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(default=None, max_length=39, null=True, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('user_agent_is_regular_expression', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reason', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('reason_is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('blockthem', ['Rule'])


    def backwards(self, orm):
        
        # Deleting model 'Rule'
        db.delete_table('blockthem_rule')


    models = {
        'blockthem.rule': {
            'Meta': {'object_name': 'Rule'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'default': 'None', 'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reason_is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'user_agent_is_regular_expression': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['blockthem']
