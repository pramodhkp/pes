from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from college.models import Project, Student, Teacher, Evaluation
import random


def get_student_projects(user, id):
	userProjects = []
	projects = Project.objects.all()
	for project in projects:
		if user in project.members_s.filter(s_id=id):
			userProjects.append(project)
	return userProjects

def get_teacher_projects(user, id):
	userProjects = []
	projects = Project.objects.all()
	for project in projects:
		if user in project.members_t.filter(t_id=id):
			userProjects.append(project)
	return userProjects

def update_project_progress(projects):
	for project in projects:
		panelLength = len(project.members_t.all())
		evals = Evaluation.objects.filter(project=project)
		sum = 0
		for e in evals:
			sum = sum+e.progress
		if(panelLength != 0):
			avg = sum/panelLength
			if(avg > 100):
				avg = 100
			project.progress = avg
		else:
			project.progress = 0
		project.save()

def main(request):
	return render(request, "home.html")

# Authorize the user with USN and password
# Check whether the logged in user is a teacher/student and redirect accordingly.
def login(request):
	if request.method == 'GET':
		return render(request, "login.html")
	else:
		userid = request.POST['userid']
		password = request.POST['password']

		try :
			user = authenticate(username=userid, password=password)
		except User.DoesNotExist:
			print 'user does not exist'
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
			error = True
			return render(request, "login.html", {'error': error})


# Redirect user to his respective home URL
@login_required(login_url='/college/login/')
def home(request):
	if hasattr(request.user, 'student'):
		return redirect('/college/student/')
	else:
		return redirect('/college/teacher/')


@login_required(login_url='/college/login/')
def project_list_student(request):
	user = request.user.student
	name = user.first_name + ' ' + user.last_name
	studentFlag = True
	id = user.s_id
	userProjects = get_student_projects(user, id)
	finProjects = []
	ongProjects = []
	for project in userProjects:
		if project.progress != 100:
			ongProjects.append(project)
		else:
			finProjects.append(project)

	for project in userProjects:
		evals = project.evaluation_set.all()

	return render(request, "projectlist.html", {'student': studentFlag, 'finProjects': finProjects, 'ongProjects': ongProjects,
												 'name': name, 'evals': evals})


@login_required(login_url='/college/login/')
def project_list_teacher(request):
	user = request.user.teacher
	name = user.first_name + ' ' + user.last_name
	teacherFlag = True
	id = user.t_id
	userProjects = get_teacher_projects(user, id)
	finProjects = []
	ongProjects = []
	for project in userProjects:
		if project.progress != 100:
			ongProjects.append(project)
		else:
			finProjects.append(project)

	for project in userProjects:
		evals = project.evaluation_set.all()

	return render(request, "projectlist.html", { 'teacher': teacherFlag, 'finProjects': finProjects, 'ongProjects': ongProjects,
												 'name': name, 'evals': evals})



# Responsible for teacher dashboard. Sends details about projects under a teacher.
@login_required(login_url='/college/login/')
def dashboard_teacher(request):
	user = request.user.teacher
	name = user.first_name + ' ' + user.last_name
	teacherFlag = True
	id = user.t_id
	userProjects = get_teacher_projects(user, id)
	finished = 0
	ongoing = 0
	evals = []
	for project in userProjects:
		if project.progress == 100:
			finished += 1
		else:
			ongoing += 1
	if userProjects:
		randProject = userProjects[0]
		evals = randProject.evaluation_set.all()
	return render(request, "dashboard.html", {'teacher': user, 'name' : name,
													'projects': userProjects, 'fincount': finished, 
													'ongcount': ongoing, 'evals': evals })

# Responsible for student dashboard. Sends details about projects under a student.
@login_required(login_url='/college/login/')
def dashboard_student(request):
	user = request.user.student
	name = user.first_name + ' ' + user.last_name
	studentFlag = True
	id = user.s_id
	userProjects = get_student_projects(user, id)
	finished = 0
	ongoing = 0
	evals = []
	for project in userProjects:
		if project.progress == 100:
			finished += 1
		else:
			ongoing += 1
	if userProjects:
		randProject = userProjects[0]
		evals = randProject.evaluation_set.all()
	return render(request, "dashboard.html", {'student': user, 'name' : name,
													'projects': userProjects, 'fincount': finished, 'ongcount': ongoing,
													'evals': evals })

# Student profile
@login_required(login_url='/college/login/')
def profile_student(request, id):
	user = request.user.student
	name = user.first_name + ' ' + user.last_name
	profile = Student.objects.get(s_id = id)
	projects = get_student_projects(user, id)
	return render(request, "profile.html", {'name' : name, 'profile': profile,
												'projects': projects})
# Teacher profile
@login_required
def profile_teacher(request, id):
	user = request.user.teacher
	name = user.first_name + ' ' + user.last_name
	profile = Teacher.objects.get(t_id = id)
	projects = get_teacher_projects(user, id)
	return render(request, "profile.html", {'name' : name, 'profile': profile,
												'projects': projects})

# Detaisl about the project, including evaluations
@login_required(login_url='/college/login/')
def project_details(request, id):
	user = None
	if hasattr(request.user, 'student'):
		user = request.user.student
	else:
		user = request.user.teacher
	name = user.first_name + ' ' + user.last_name
	project = Project.objects.get(p_id = id)
	evals = project.evaluation_set.all()
	return render(request, "projects.html", {'name' : name, 'project' : project,
												 'evals': evals})

# Get inputs from the evaluation form, find average and update Evaluation model
# Update all projects with the new progress.
@login_required(login_url='/college/login/')
def evaluate_project(request, id):
	if request.method == 'GET':
		user = request.user.teacher
		name = user.first_name+ ' '+ user.last_name
		project = Project.objects.get(p_id = id)
		return render(request, "evaluationform.html", {'name': name, 'project': project })
	else:
		sum = 0
		user = request.user.teacher
		submission = int(request.POST['submission'])
		output = int(request.POST['output'])
		research = int(request.POST['research'])
		quality = int(request.POST['quality'])
		presentation = int(request.POST['presentation'])
		sum = submission + output + quality + research + presentation
		length = len(request.POST) -2
		average = int(sum)/length
		project = Project.objects.get(p_id=id)
		progress = request.POST['progress']
		e = Evaluation(project=project, submission=submission, output= output, research=research,
							 quality= quality, presentation=presentation, evaluator=user,
							 		progress=progress, score=int(average))
		e.save()
		projects = Project.objects.all()
		update_project_progress(projects)
		return redirect("/college/teacher/")


# Edit profile
@login_required(login_url='/college/login/')
def edit_profile(request):
	return render(request, 'edit_profile.html')

# logs out user
@login_required(login_url='/college/login/')
def logout(request):
	auth_logout(request)
	return render(request, "home.html")


