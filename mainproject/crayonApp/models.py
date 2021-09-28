from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=50, null=False)
    email = models.EmailField()

class QuizType(models.Model):
    name =  models.CharField(max_length=50, null=False)

class Quiz(models.Model):
    choice_text = models.CharField(max_length=200)
    type =  models.ForeignKey(QuizType, on_delete=models.CASCADE)

class Response(models.Model):
    choice_text = models.CharField(max_length=200, default = "Perfect")
    votes = models.IntegerField(default=0)

 