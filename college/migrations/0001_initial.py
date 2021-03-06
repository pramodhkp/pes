# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'college_student', (
            ('s_auth', self.gf('django.db.models.fields.related.OneToOneField')(default='None', to=orm['auth.User'], unique=True)),
            ('s_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=70)),
        ))
        db.send_create_signal(u'college', ['Student'])

        # Adding model 'Teacher'
        db.create_table(u'college_teacher', (
            ('t_auth', self.gf('django.db.models.fields.related.OneToOneField')(default='None', to=orm['auth.User'], unique=True)),
            ('t_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=70)),
        ))
        db.send_create_signal(u'college', ['Teacher'])

        # Adding model 'Project'
        db.create_table(u'college_project', (
            ('p_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('details', self.gf('django.db.models.fields.TextField')()),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('progress', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'college', ['Project'])

        # Adding M2M table for field members_s on 'Project'
        m2m_table_name = db.shorten_name(u'college_project_members_s')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'college.project'], null=False)),
            ('student', models.ForeignKey(orm[u'college.student'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'student_id'])

        # Adding M2M table for field members_t on 'Project'
        m2m_table_name = db.shorten_name(u'college_project_members_t')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'college.project'], null=False)),
            ('teacher', models.ForeignKey(orm[u'college.teacher'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'teacher_id'])

        # Adding model 'Evaluation'
        db.create_table(u'college_evaluation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['college.Project'])),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('progress', self.gf('django.db.models.fields.IntegerField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'college', ['Evaluation'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'college_student')

        # Deleting model 'Teacher'
        db.delete_table(u'college_teacher')

        # Deleting model 'Project'
        db.delete_table(u'college_project')

        # Removing M2M table for field members_s on 'Project'
        db.delete_table(db.shorten_name(u'college_project_members_s'))

        # Removing M2M table for field members_t on 'Project'
        db.delete_table(db.shorten_name(u'college_project_members_t'))

        # Deleting model 'Evaluation'
        db.delete_table(u'college_evaluation')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'college.evaluation': {
            'Meta': {'object_name': 'Evaluation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'progress': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Project']"}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'college.project': {
            'Meta': {'object_name': 'Project'},
            'details': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'members_s': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['college.Student']", 'symmetrical': 'False'}),
            'members_t': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['college.Teacher']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'p_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'progress': ('django.db.models.fields.IntegerField', [], {})
        },
        u'college.student': {
            'Meta': {'object_name': 'Student'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '70'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            's_auth': ('django.db.models.fields.related.OneToOneField', [], {'default': "'None'", 'to': u"orm['auth.User']", 'unique': 'True'}),
            's_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'college.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '70'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            't_auth': ('django.db.models.fields.related.OneToOneField', [], {'default': "'None'", 'to': u"orm['auth.User']", 'unique': 'True'}),
            't_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['college']