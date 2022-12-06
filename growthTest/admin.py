from django.contrib import admin
from .models import *

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Question._meta.fields]

admin.site.register(Question, QuestionAdmin)