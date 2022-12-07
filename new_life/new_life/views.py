from django.shortcuts import render
from django.http import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . forms import LoginForm
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, 'index.html', {'name': 'Nihaal'})


