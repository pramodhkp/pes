from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
	s_auth = models.OneToOneField(User, default='None')
	s_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=70)


class Teacher(models.Model):
	t_auth = models.OneToOneField(User, default='None')
	t_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=70)

class Project(models.Model):
	p_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	details = models.TextField()
	members_s = models.ManyToManyField(Student)
	members_t = models.ManyToManyField(Teacher)
	comments = models.TextField()

