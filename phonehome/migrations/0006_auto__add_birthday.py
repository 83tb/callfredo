# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Birthday'
        db.create_table('phonehome_birthday', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('call', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['phonehome.Call'])),
            ('recording', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['phonehome.Recording'], null=True, blank=True)),
            ('recipient_fb_name', self.gf('django.db.models.fields.CharField')(max_length=240)),
            ('recipient_fb_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('phonehome', ['Birthday'])


    def backwards(self, orm):
        # Deleting model 'Birthday'
        db.delete_table('phonehome_birthday')


    models = {
        'accounts.user': {
            'Meta': {'object_name': 'User', '_ormbases': ['auth.User']},
            'calling_hour': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'calling_minute': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_call_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 10, 15, 0, 0)'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'phonehome.birthday': {
            'Meta': {'object_name': 'Birthday'},
            'call': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['phonehome.Call']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient_fb_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'recipient_fb_name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'recording': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['phonehome.Recording']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'phonehome.call': {
            'Meta': {'object_name': 'Call'},
            'data': ('phonehome.utils.JSONField', [], {'default': "'{}'", 'json_type': 'dict'}),
            'fetched_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.User']"})
        },
        'phonehome.recording': {
            'Meta': {'object_name': 'Recording'},
            'call_sid': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'caller': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'fb_user_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        }
    }

    complete_apps = ['phonehome']