from django.contrib import admin

from .models import QuizType, Quiz, QuizSubtype

admin.site.register(QuizType)
admin.site.register(Quiz)
admin.site.register(QuizSubtype)
