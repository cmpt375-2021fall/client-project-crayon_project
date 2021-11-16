from . import views
from django.contrib import admin
from django.urls import include, path


app_name = 'crayonApp'
urlpatterns = [
    path('quiz/', views.quiz, name = 'quiz'),
]
