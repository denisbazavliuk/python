#coding=utf-8
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def login(request):
	context = {}
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username = username, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			context['login_error'] = u'Пользователь не найден'
			return render(request, 'userauth/login.html', context)
	else:
		return render(request, 'userauth/login.html', context)

def logout(request):
	auth.logout(request)
	return redirect('/')


def register(request):
	context = {}
	context['form'] = UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.save()
			newuser = auth.authenticate(username = newuser_form.cleaned_data['username'], password = newuser_form.cleaned_data['password1'])
			auth.login(request, newuser)
			return redirect('login')
		else:
			context['form'] = newuser_form
	return render(request, 'userauth/register.html', context)


