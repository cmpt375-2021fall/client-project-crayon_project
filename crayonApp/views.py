from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from . import models
from . import forms
from .models import File, Room
from .forms import FileUploadModelForm
import os
import uuid
from .test import html_to_string
from django.urls import reverse
import random
from django.template.loader import get_template
from django.template.defaultfilters import filesizeformat
from .send_mail import sendEmail


def index(request):
    return render(request, 'crayonApp/index.html')
 
def admin_login(request):
    return render(request, 'crayonApp/admin_login.html')

def userportal(request):
    if not request.session.get('is_login', None):  
      return redirect('/login/')
    return render(request, 'crayonApp/userportal.html')



def login(request):
    if request.session.get('is_login', None):  #no repeat login
      return redirect('/userportal/')
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
                return redirect('/userportal/')
            else:
                message = 'Password is not matched with the account'
                return render(request, 'crayonApp/login.html', locals())
      else:
           return render(request, 'crayonApp/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'crayonApp/login.html', locals())

def register(request):
    if request.session.get('is_login', None):
        return redirect('userportal')

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
def file_list_host(request):
    room_id = request.session['room_id']
    room = models.Room.objects.get(room_id=room_id)
    file_attrs = models.File_attr.objects.filter(room_id = room)
    files = []
    for fa in file_attrs:
        files.append(fa.file_id)
    
    return render(request, 'crayonApp/file_list_host.html', {'files': files})

def file_list_guest(request):
    room_id = request.session['room_id']
    room = models.Room.objects.get(room_id=room_id)
    file_attrs = models.File_attr.objects.filter(room_id = room)
    files = []
    for fa in file_attrs:
        files.append(fa.file_id)
    
    return render(request, 'crayonApp/file_list_guest.html', {'files': files})

def project_guest(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    elif not request.session.get('room_id', None):
        return redirect('/room_enter/')

    return render(request, 'crayonApp/project_guest.html')

def code_list(request):
    user = get_object_or_404(models.User, pk= request.session['user_id'])
    rooms = user.room_set.all()

    return render(request, 'crayonApp/code_list.html',{
            'rooms': rooms,
        }) 

def project_host(request):
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
            return redirect("/project_host/")
    else:
        form = FileUploadModelForm()

    return render(request, 'crayonApp/project_host.html', {'form': form,
                                                            'heading': 'Upload files with ModelForm'})


def room_enter(request):
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
                request.session['room_creater_email'] = room.room_creater.email
                request.session['room_quiz_score'] = {
               "COLOR":0,
               "CONTRAST":0,
               "REPETITION":0,
               "ARRANGEMENT":0,
               "WHY":0,
               "ORGANIZATION":0,
               "NEGATIVE SPACE":0,
               "TYPOGRAPHY":0,
               "ICONOGRAPHY":0,
               "PHOTOGRAPHY":0,
           }
                return redirect('/project_guest/')
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
           new_room.room_creater = models.User.objects.get(email=request.session['user_email'])
           new_room.save()
           room_id = getattr(new_room, 'room_id')
           request.session['room_id'] = room_id
           request.session['room_name'] = name
           request.session['room_creater_email'] =  request.session['user_email']
           request.session['room_quiz_score'] = {
               "COLOR":0,
               "CONTRAST":0,
               "REPETITION":0,
               "ARRANGEMENT":0,
               "WHY":0,
               "ORGANIZATION":0,
               "NEGATIVE SPACE":0,
               "TYPOGRAPHY":0,
               "ICONOGRAPHY":0,
               "PHOTOGRAPHY":0,
           }
           return redirect("/project_host/")
        else:
            return render(request, 'crayonApp/room_create.html', locals())
    
    create_form = forms.CreateForm()
    return render(request, 'crayonApp/room_create.html', locals())
        


def detail(request, quiz_id):
    quiz = get_object_or_404(models.Quiz, id=quiz_id)
    try:
        selected_choice = quiz.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'crayonApp/detail.html', {
            'quiz': quiz,
        })
    else:
        quiz_type = quiz.quiz_subtype.type.name
        # only add valuable score
        if(selected_choice.score>=0):
            scores =  request.session['room_quiz_score']
            scores[quiz_type] += selected_choice.score
            request.session['room_quiz_score'] = scores
        if quiz.id <  len(models.Quiz.objects.all()):
            return HttpResponseRedirect(reverse('detail', args=(quiz.id+1,)))
        else:
            return HttpResponseRedirect(reverse('result'))

def result(request):
    return render(request, 'crayonApp/result.html')

def report(request):
    t = get_template('crayonApp/result.html')

    html = t.render({'request':request})
    file_path = './crayonApp/static/reports/'+ str(request.session['user_id'])+'_'+str(random.randint(0,100))+'.pdf'
    html_to_string(html, file_path)
    sendEmail(request.session['room_creater_email'], file_path)
    return render(request, 'crayonApp/report.html')
