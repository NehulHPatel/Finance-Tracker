# authentication/views.py

from django.shortcuts import render

def welcome(request):
    return render(request, 'authentication/welcome.html')

def signup(request):
    return render(request, 'authentication/signup.html')

def login(request):
    return render(request, 'authentication/login.html')

def base(request):
    return render(request, 'base.html')
