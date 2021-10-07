from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import User


def index(request):
    pass
    return render(request,'crayonApp/index.html')

def login(request):
    pass
    return render(request,'crayonApp/login.html')