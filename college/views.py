from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request, "home.html")


def login(request):
	if request.method == 'GET':
		return render(request, "login.html")
	else:
		email = request.POST['email']
		password = request.POST['password']
		
		try :			
			user = authenticate(email=email, password=password)
		except User.DoesNotExist:
			error = True
			return render(request, "login.html", {'error': error});
		
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				name = user.first_name + ' ' + user.last_name
				return redirect('/college/main/')
			else:
				pass
		else:		
			return render(request, "login.html")	


@login_required(login_url='/college/login/')
def dashboard(request):
	name = request.user.first_name + ' ' + request.user.last_name
	return render(request, "dashboard.html", {'name': name})
	

@login_required(login_url='/college/login/')
def logout(request):
	auth_logout(request)
	return render(request, "home.html")