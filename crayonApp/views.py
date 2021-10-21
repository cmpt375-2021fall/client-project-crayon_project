from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
from . import forms


def index(request):
    pass
    return render(request,'crayonApp/index.html')

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
                return redirect('/')
            else:
                message = 'Password is not matched with the account'
                return render(request, 'crayonApp/login.html', locals())
      else:
           return render(request, 'crayonApp/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'crayonApp/login.html', locals())


def register(request):
    pass
    return render(request,'crayonApp/register.html')

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")