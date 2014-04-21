from django.db import models
from django.contrib.auth.models import User

# Creates a Student table in the database
class Student(models.Model):
	s_auth = models.OneToOneField(User, default='None')
	s_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=70)

	def __unicode__(self):
		return 'Student:'+ ' ' + self.first_name + ' ' + self.last_name

# Creates a Teacher table in the database
class Teacher(models.Model):
	t_auth = models.OneToOneField(User, default='None')
	t_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=70)

	def __unicode__(self):
		return 'Teacher:'+ ' ' + self.first_name + ' ' + self.last_name

# Creates a Project table in the database
class Project(models.Model):
	p_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	details = models.TextField()
	members_s = models.ManyToManyField(Student)
	members_t = models.ManyToManyField(Teacher)
	duration = models.IntegerField(help_text='In months')
	progress = models.IntegerField(help_text='In percentage')
	file = models.FileField(upload_to='uploads/%Y/%m/%d/')

	def __unicode__(self):
		return 'Project:'+ ' ' + self.name

# Creates a Evaluation  table in the database
class Evaluation(models.Model):
	project = models.ForeignKey(Project)
	evaluator = models.ForeignKey(Teacher)
	submission = models.IntegerField(help_text="B/w 1 -100")
	quality = models.IntegerField(help_text="B/w 1 -100")
	output = models.IntegerField(help_text="B/w 1 -100")
	research = models.IntegerField(help_text="B/w 1 -100")
	presentation = models.IntegerField(help_text="B/w 1 -100")
	score = models.IntegerField(help_text ='In percentage')
	progress = models.IntegerField(help_text='In percentage')
	timestamp = models.DateTimeField(auto_now_add=True)


