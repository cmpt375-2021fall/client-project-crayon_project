from django.contrib import admin

from .models import QuizType, Quiz, QuizSubtype, User, File, Room

admin.site.register(QuizType)
admin.site.register(Quiz)
admin.site.register(QuizSubtype)
admin.site.register(User)
admin.site.register(File)
admin.site.register(Room)


