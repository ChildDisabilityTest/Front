from django.db import models

# Create your models here.
class Question(models.Model):

    GROUP_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )

    COLUMN_CHOICES = (
        ('body', '신체'),
        ('recognition', '인지'),
        ('language', '언어'),
        ('emotion', '정서'),
        ('sociality', '사회성'),
        ('autism', '자폐경향성'),
        ('adhd', 'ADHD경향성'),
    )
    
    number = models.IntegerField(primary_key=True, help_text="질문번호")
    content = models.CharField(max_length=100, null=True, blank=True, help_text="질문내용")
    test_column = models.CharField(max_length=11, choices=COLUMN_CHOICES, null=True, blank=True, help_text="규준표 컬럼")
    group = models.CharField(max_length=1, choices=GROUP_CHOICES, null=True, blank=True, help_text="질문그룹")