# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Teacher'
        db.create_table(u'college_teacher', (
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
            ('comments', self.gf('django.db.models.fields.TextField')()),
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

        # Adding model 'Student'
        db.create_table(u'college_student', (
            ('s_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=70)),
        ))
        db.send_create_signal(u'college', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Teacher'
        db.delete_table(u'college_teacher')

        # Deleting model 'Project'
        db.delete_table(u'college_project')

        # Removing M2M table for field members_s on 'Project'
        db.delete_table(db.shorten_name(u'college_project_members_s'))

        # Removing M2M table for field members_t on 'Project'
        db.delete_table(db.shorten_name(u'college_project_members_t'))

        # Deleting model 'Student'
        db.delete_table(u'college_student')


    models = {
        u'college.project': {
            'Meta': {'object_name': 'Project'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'details': ('django.db.models.fields.TextField', [], {}),
            'members_s': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['college.Student']", 'symmetrical': 'False'}),
            'members_t': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['college.Teacher']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'p_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'college.student': {
            'Meta': {'object_name': 'Student'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '70'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            's_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'college.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '70'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            't_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['college']