from django.shortcuts import render
from User.models import User
from django.http import HttpResponse

def user_signup_save(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = User(fname = fname, lname = lname, email = email, password = password)
    user.save()
    return HttpResponse(User.objects.all())
# Create your views here.
