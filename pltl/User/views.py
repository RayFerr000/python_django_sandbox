from django.shortcuts import render,redirect
from User.models import User
from django.http import HttpResponse
from django.contrib import auth

def user_signup_save(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = User.objects.create_user(fname = fname, lname = lname, email = email, password = password)
    
    return redirect('home')


def login(request):
	email = request.POST.get('email')
	password = request.POST.get('password')
	user = auth.authenticate(email = email , password = password)
	
	if user is not None:
		auth.login(request, user)
		return render(request, 'user_home.html')
	else:
		return HttpResponse("invalid, not logged in")
	

# Create your views here.
