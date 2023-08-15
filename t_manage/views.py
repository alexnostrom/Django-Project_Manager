from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db.utils import IntegrityError
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import get_user_model
from .backend import EmailBackend

User = get_user_model()


def main_page(request):
	return render(request, 'main_page.html', {'title': 'Main_page'})


def loginuser(request):
	if request.method == 'GET':
		return render(request, 'loginuser.html', {'title': 'Login Form', 'forms': UserLoginForm()})
	else:
		user = EmailBackend()
		user = user.authenticate(request, username=request.POST['email'])

		if user is None:
			return render(request, 'loginuser.html',
						  {'forms': UserLoginForm(), 'title': 'Login Form', 'error': 'User not Found!'})
		elif user.password != request.POST['password']:
			return render(request, 'loginuser.html',
						  {'forms': UserLoginForm(), 'title': 'Login Form', 'error': 'Wrong password or Username!'})

		else:
			login(request, user)
			return redirect('projects_show_page:project_show_main_page')


def signupuser(request):
	if request.method == 'GET':
		return render(request, 'signupuser.html', {'title': 'Registration Form', 'forms': UserRegistrationForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			userform = UserRegistrationForm(request.POST)
			if userform.is_valid():
				try:
					if User.objects.get(email=request.POST['email']):
						raise IntegrityError
					else:
						user = User.objects.create(username=request.POST['username'],
												   last_name=request.POST['lastname'], age=request.POST['age'],
												   email=request.POST['email'],
												   password=request.POST['password1'])
				except IntegrityError:
					return render(request, 'signupuser.html',
								  {'forms': UserRegistrationForm(), 'title': 'SignUp',
								   'error': 'User Already Exist!'})
				else:
					user.save()
					login(request, user)
					return redirect('projects_show_page:project_show_main_page')
			else:
				return render(request, 'signupuser.html',
							  {'forms': UserRegistrationForm(), 'title': 'SignUp',
							   'error': 'User Already Exist!'})
		else:
			return render(request, 'signupuser.html',
						  {'forms': UserRegistrationForm(), 'title': 'SignUp', 'error': 'Passwords did not match'})
