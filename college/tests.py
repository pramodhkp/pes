from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from college.models import Student, Teacher
# Create your tests here.


class LoginTest(TestCase):
	def setUp(self):
		user_s = User.objects.create_user(username='studenttest', password='pkp')
		student = Student.objects.create(s_auth=user_s, s_id=1, first_name="Pramodh", last_name="KP", email="prmdh1@gmail.com")
		user_t = User.objects.create_user(username='teachertest', password='pkp')
		teacher = Teacher.objects.create(t_auth=user_t, t_id=1, first_name="Pramodh", last_name="KP", email="prmdh1@gmail.com")


	def test_student_login(self):
		c = Client()
		res = c.get('/college/login/')
		response = c.post('/college/login/', {'userid' : 'studenttest', 'password': 'pkp' }, follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertRedirects(response, '/college/student/')
		invalResponse = c.post('/college/login/', {'userid' : 'wrongtest', 'password' : 'pkp'}, follow=True)
		self.assertEqual(invalResponse.status_code, 200)

	def test_teacher_login(self):
		c = Client()
		res = c.get('/college/login/')
		response = c.post('/college/login/', {'userid' : 'teachetest', 'password': 'pkp' }, follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertRedirects(response, '/college/teacher/')
		invalResponse = c.post('/college/login/', {'userid' : 'wrongtest', 'password' : 'pkp'}, follow=True)
		self.assertEqual(invalResponse.status_code, 200)

class EvaluationTest(TestCase):
	def test_eval_valid(self):
		self.assertEqual(True, True)

	def test_eval_invalid(self):
		self.assertEqual(True, True)

class SearchTest(TestCase):
	def test_search_valid(self):
		self.assertEqual(True, True)

	def test_search_invalid(self):
		self.assertEqual(True, True)




