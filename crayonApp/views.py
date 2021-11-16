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

def take_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    student = request.user.student

    if student.quizzes.filter(pk=pk).exists():
        return render(request, 'students/taken_quiz.html')

    total_questions = quiz.questions.count()
    unanswered_questions = student.get_unanswered_questions(quiz)
    total_unanswered_questions = unanswered_questions.count()
    progress = 100 - round(((total_unanswered_questions - 1) / total_questions) * 100)
    question = unanswered_questions.first()

    if request.method == 'POST':
        form = TakeQuizForm(question=question, data=request.POST)
        if form.is_valid():
            with transaction.atomic():
                student_answer = form.save(commit=False)
                student_answer.student = student
                student_answer.save()
                if student.get_unanswered_questions(quiz).exists():
                    return redirect('students:take_quiz', pk)
                else:
                    correct_answers = student.quiz_answers.filter(answer__question__quiz=quiz, answer__is_correct=True).count()
                    percentage = round((correct_answers / total_questions) * 100.0, 2)
                    TakenQuiz.objects.create(student=student, quiz=quiz, score=correct_answers, percentage= percentage)
                    student.score = TakenQuiz.objects.filter(student=student).aggregate(Sum('score'))['score__sum']
                    student.save()
                    if percentage < 50.0:
                        messages.warning(request, 'Better luck next time! Your score for the quiz %s was %s.' % (quiz.name, percentage))
                    else:
                        messages.success(request, 'Congratulations! You completed the quiz %s with success! You scored %s points.' % (quiz.name, percentage))
                    # return redirect('students:quiz_list')
                    return redirect('students:student_quiz_results', pk)
    else:
        form = TakeQuizForm(question=question)

    return render(request, 'classroom/students/take_quiz_form.html', {
        'quiz': quiz,
        'question': question,
        'form': form,
        'progress': progress,
        'answered_questions': total_questions - total_unanswered_questions,
        'total_questions': total_questions
    })
