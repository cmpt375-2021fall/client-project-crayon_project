"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from crayonApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('crayonApp/', include('crayonApp.urls')),
    path('admin/', admin.site.urls),
     # ex: /crayonApp/
    path('', views.index, name='index'),
    # ex: /crayonApp/login/
    path('login/', views.login, name='login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout, name = 'logout'),
    path('room_create/', views.room_create, name = 'room_create'),
    path('room_enter/', views.room_enter, name = 'room_enter'),
     # Upload Files Using Model Form
    re_path(r'^upload/$', views.model_form_upload, name='model_form_upload'),
    # View File List
    path('file_list/', views.file_list, name='file_list'),
<<<<<<< HEAD
    path('admin_login/', views.admin_login, name='admin_login'),
=======
>>>>>>> deploy
    path('quiz/', views.quiz, name='quiz'),
    path('<int:quiz_id>/', views.detail, name='detail'),
    path('result/', views.result, name='result'),
    path('userportal/', views.userportal, name='userportal'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)