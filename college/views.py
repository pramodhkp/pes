from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from college.models import Project

def home(request):
	return render(request, "home.html")

def login(request):
	if request.method == 'GET':
		return render(request, "login.html")
	else:
		userid = request.POST['userid']
		password = request.POST['password']

		try :
			user = authenticate(username=userid, password=password)
		except User.DoesNotExist:
			error = True
			return render(request, "login.html", {'error': error});

		if user is not None:
			if user.is_active:
				auth_login(request, user)
				try:
					if user.teacher is not None:
						return redirect('/college/teacher/')
				except ObjectDoesNotExist:
					return redirect('/college/student/')
			else:
				pass
		else:
			return render(request, "login.html")


@login_required(login_url='/college/login/')
def dashboard_teacher(request):
	user = request.user.teacher
	name = user.first_name + ' ' + user.last_name
	projects = Project.objects.get('mem')
	print projects
	teacher = True
	return render(request, "dashboard.html", {'teacher': teacher, 'name' : name})

@login_required(login_url='/college/login/')
def dashboard_student(request):
	user = request.user.student
	name = user.first_name + ' ' + user.last_name
	print request.user, name
	student = True
	return render(request, "dashboard.html", {'student': student, 'name' : name})

@login_required(login_url='/college/login/')
def logout(request):
	auth_logout(request)
	return render(request, "home.html")
