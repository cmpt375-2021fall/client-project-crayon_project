from django.db import models
import os
import uuid

class User(models.Model):
    username = models.CharField(max_length=128, null=False)
    password = models.CharField(max_length=256, null=False)
    email = models.EmailField(unique = True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class QuizType(models.Model):
    name =  models.CharField(max_length=50, null=False)
    
class QuizSubtype(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=500, null=False)
    type =  models.ForeignKey(QuizType, on_delete=models.CASCADE)

class Quiz(models.Model):
    choice_text = models.CharField(max_length=200)
    quiz_subtype =  models.ForeignKey(QuizSubtype, on_delete=models.CASCADE, null=True, default = None)

class Response(models.Model):
    choice_text = models.CharField(max_length=200, default = "Perfect")
    votes = models.IntegerField(default=0)

class Room(models.Model):
    room_id = models.CharField(primary_key=True, unique=True, max_length=256, default=uuid.uuid4().hex[:8], editable=False)
    name = models.CharField(max_length=256, null=False, default = " " )
    c_time = models.DateTimeField(auto_now_add=True)


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)


class File(models.Model):
    f_id = models.CharField(primary_key=True, unique=True, max_length=256, default=uuid.uuid4().hex[:8], editable=False)
    file = models.FileField(upload_to=user_directory_path, null=True)

class File_attr(models.Model):
    file_id = models.ForeignKey(File, on_delete=models.CASCADE, null=True, default = None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default = None)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, default = None)

    
