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
    path('admin_login/', views.admin_login, name='admin_login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout, name = 'logout'),
    path('room_create/', views.room_create, name = 'room_create'),
    path('room_enter/', views.room_enter, name = 'room_enter'),
    path('code_list/', views.code_list, name = 'code_list'),
     # Upload Files Using Model Form
    re_path(r'^project_host/$', views.project_host, name='project_host'),
    path('project_guest/', views.project_guest, name='project_guest'),
    # View File List
    path('file_list_host/', views.file_list_host, name='file_list_host'),
    path('file_list_guest/', views.file_list_guest, name='file_list_guest'),
    path('<int:quiz_id>/', views.detail, name='detail'),
    path('result/', views.result, name='result'),
    path('userportal/', views.userportal, name='userportal'),
    path('report/', views.report, name ='report'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)