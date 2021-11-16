from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
from . import forms


def index(request):
   if not request.session.get('is_login', None):
        return redirect('/login/')
   return render(request, 'crayonApp/index.html')

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


def quiz(request):
   if not request.session.get('null', None):
        return redirect('/quiz/')
   return render(request, 'crayonApp/quiz.html')