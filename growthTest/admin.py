from django.contrib import admin
from .models import *

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Question._meta.fields]
class AnswerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Answer._meta.fields]
class CommentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Comment._meta.fields]
class CriterionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Criterion._meta.fields]
class ResultAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Result._meta.fields]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Criterion, CriterionAdmin)
admin.site.register(Result, ResultAdmin)