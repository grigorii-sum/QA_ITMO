from django.contrib import admin
from .models import ExtendedUser, Question, Answer


admin.site.register(ExtendedUser)
admin.site.register(Question)
admin.site.register(Answer)
