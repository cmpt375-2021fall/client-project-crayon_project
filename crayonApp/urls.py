from django.urls import path

from . import views
app_name = 'crayonApp'
urlpatterns = [
    # ex: /crayonApp/
    path('', views.index, name='index'),
    # ex: /crayonApp/login/
    path('login/', views.login, name='login'),
]

