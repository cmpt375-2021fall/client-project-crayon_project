from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
from . import forms
from .models import File, Room
from .forms import FileUploadModelForm
import os
import uuid
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'crayonApp/index.html')

def landing(request):
    return render(request, 'crayonApp/landing.html')

def quiz(request):
    return render(request, 'crayonApp/quiz.html')

def userportal(request):
    return render(request, 'crayonApp/userportal.html')



def login(request):
    if request.session.get('is_login', None):  #no repeat login
      return redirect('/')
    if request.method == "POST":
      login_form = forms.UserForm(request.POST)
      message = 'Please check your input'
      if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(email=email)
            except:
                  message = 'User does not exit'
                  return render(request, 'crayonApp/login.html', locals())
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                request.session['user_name'] = user.username
                return redirect('/')
            else:
                message = 'Password is not matched with the account'
                return render(request, 'crayonApp/login.html', locals())
      else:
           return render(request, 'crayonApp/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'crayonApp/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = 'Please check your input'
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')

            if password1 != password2:
                message = 'Tow passwords are different'
                return render(request, 'crayonApp/register.html', locals())
            else:
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'Account already exited'
                    return render(request, 'crayonApp/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)

                new_user = models.User()
                new_user.username = username
                new_user.password = password1
                new_user.email = email
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'crayonApp/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'crayonApp/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")

# Show file list
def file_list(request):
    room_id = request.session['room_id']
    room = models.Room.objects.get(room_id=room_id)
    file_attrs = models.File_attr.objects.filter(room_id = room)
    files = []
    for fa in file_attrs:
        files.append(fa.file_id)
    
    return render(request, 'crayonApp/file_list.html', {'files': files})

def model_form_upload(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    elif not request.session.get('room_id', None):
        return redirect('/room_enter/')
    if request.method == "POST":
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            room_id = request.session['room_id']
            room = models.Room.objects.get(room_id=room_id)
            user_id = request.session['user_id']
            user = models.User.objects.get(id=user_id)

            new_file_attr = models.File_attr()
            new_file_attr.file_id = file
            new_file_attr.room_id = room
            new_file_attr.user_id = user
            new_file_attr.save()
            return redirect("/upload/")
    else:
        form = FileUploadModelForm()

    return render(request, 'crayonApp/upload_form.html', {'form': form,
                                                            'heading': 'Upload files with ModelForm'})

def room_enter(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.method == "POST":
        enter_form = forms.EnterForm(request.POST)
        message = 'Please check your input'
        if enter_form.is_valid():
            room_id = enter_form.cleaned_data.get('room_id')
            try:
                room = models.Room.objects.get(room_id=room_id)
            except:
                message = 'Room does not exit'
                return render(request, 'crayonApp/room_enter.html', locals())
            if room.room_id == room_id:
                request.session['room_id'] = room.room_id
                return redirect('/upload/')
            else:
                return render(request, 'crayonApp/room_enter.html')

    enter_form = forms.EnterForm()
    return render(request, 'crayonApp/room_enter.html', locals())

def room_create(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.method == "POST":
        create_form = forms.CreateForm(request.POST)
        if create_form.is_valid():
           name = create_form.cleaned_data.get('name')

           new_room = models.Room()
           new_room.name = name
           new_room.save()
           room_id = getattr(new_room, 'room_id')
           request.session['room_id'] = room_id
           request.session['room_name'] = name
           return redirect("/upload/")
        else:
            return render(request, 'crayonApp/room_create.html', locals())
    
    create_form = forms.CreateForm()
    return render(request, 'crayonApp/room_create.html', locals())
        
    