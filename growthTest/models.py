from django.db import models
from user.models import Child
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Question(models.Model):

    COLUMN_CHOICES = (
        ('신체', '신체'),
        ('인지', '인지'),
        ('언어', '언어'),
        ('정서', '정서'),
        ('사회성', '사회성'),
        ('자폐경향성', '자폐경향성'),
        ('ADHD경향성', 'ADHD경향성'),
    )
    
    number = models.IntegerField(primary_key=True, help_text="질문번호")
    content = models.CharField(max_length=100, help_text="질문내용")
    column = models.CharField(max_length=7, choices=COLUMN_CHOICES, help_text="규준표 컬럼")
    age = models.IntegerField(null=True, blank=True, help_text="규준연령")

class Answer(models.Model):
    child = models.OneToOneField(Child, on_delete=models.CASCADE, related_name="answer_child", help_text="검사 아동")
    answers = ArrayField(models.IntegerField(), help_text="제출답안 리스트")

class Comment(models.Model):
    classification = models.CharField(max_length=10, help_text="분류")
    stage = models.CharField(max_length=2, help_text="단계")
    content = models.CharField(max_length=100, help_text="코멘트 내용")