from django.contrib import admin

from .models import QuizType, Quiz, QuizSubtype, User, File, Room, File_attr, Choice

admin.site.register(QuizType)
admin.site.register(Quiz)
admin.site.register(QuizSubtype)
admin.site.register(User)
admin.site.register(File)
admin.site.register(Room)
admin.site.register(File_attr)
admin.site.register(Choice)
