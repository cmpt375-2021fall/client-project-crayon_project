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
    quiz_context = models.CharField(max_length=256)
    quiz_subtype =  models.ForeignKey(QuizSubtype, on_delete=models.CASCADE, null=True, default = None)

class Choice(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, default = None)
    context = models.CharField(max_length=256, default = 0)
    score = models.IntegerField(default=0)

def _default_room_id():
    return uuid.uuid4().hex[:8]
class Room(models.Model):
    room_id = models.CharField(primary_key=True, unique=True, max_length=256, default=_default_room_id, editable=False)
    name = models.CharField(max_length=256, null=False, default = " " )
    c_time = models.DateTimeField(auto_now_add=True)
    room_creater = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default = None)
 

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)


class File(models.Model):
    file = models.FileField(upload_to=user_directory_path, null=True)

class File_attr(models.Model):
    file_id = models.ForeignKey(File, on_delete=models.CASCADE, null=True, default = None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default = None)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, default = None)

def create_superuser_if_necessary():
    # Set the name and initial password you want the superuser to have here.
    # AFTER THIS SUPERUSER IS CREATED ON HEROKU, YOU ***MUST*** IMMEDIATELY CHANGE ITS PASSWORD
    # THROUGH THE ADMIN INTERFACE. (This password is stored in cleartext in a GitHub repository,
    # so it is not acceptable to use it when there is actual client data!)
    SUPERUSER_NAME = 'admin'
    SUPERUSER_PASSWORD = 'admin'

    from django.contrib.auth.models import User

    if not User.objects.filter(username=SUPERUSER_NAME).exists():
        superuser = User(
            username=SUPERUSER_NAME,
            is_superuser=True,
            is_staff=True
        )

        superuser.save()
        superuser.set_password(SUPERUSER_PASSWORD)
        superuser.save()

    
create_superuser_if_necessary()