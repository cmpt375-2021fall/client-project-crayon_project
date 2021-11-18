from django.db import models

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
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=500, null=False)
    type =  models.ForeignKey(QuizType, on_delete=models.CASCADE)

class Quiz(models.Model):
    choice_text = models.CharField(max_length=200)
    quiz_subtype =  models.ForeignKey(QuizSubtype, on_delete=models.CASCADE, null=True, default = None)

class Response(models.Model):
    choice_text = models.CharField(max_length=200, default = "Perfect")
    votes = models.IntegerField(default=0)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField('Question')

    def __str__(self):
        return self.text

class Answer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='+') 

class TakenQuiz(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.IntegerField()
    percentage = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
 