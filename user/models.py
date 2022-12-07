from django.db import models
from django.contrib.postgres.fields import ArrayField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class IncheonRegion(models.Model):
    si = models.CharField(max_length=10, null=True, blank=True, help_text="시")
    gu = models.CharField(max_length=10, null=True, blank=True, help_text="구/군")
    emd = models.CharField(max_length=10, null=True, blank=True, help_text="읍면동")

    def __str__(self):
        return self.si + " " + self.gu + " " + self.emd


class Child(models.Model):

    GENDER_CHOICES = (
        ('M', '남자'),
        ('F', '여자')
    )

    name = models.CharField(max_length=10, null=True, blank=True, help_text="이름")
    birthDate = models.DateField(null=True, blank=True, help_text="생년월일")
    residence = models.ForeignKey(IncheonRegion, on_delete=models.CASCADE, related_name="residence", null=True, blank=True, help_text="거주지역")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, help_text="성별")
    kindergarden = models.CharField(max_length=20, null=True, blank=True, help_text="유치원 이름")
    privacy_agree = models.BooleanField(default=False, help_text="개인정보수집동의")

    def __str__(self):
        return self.name + "(" + str(self.id) + ")"


class Tester(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True, help_text="이름")
    birthDate = models.DateField(null=True, blank=True, help_text="생년월일")
    phone_number = PhoneNumberField(null=True, blank=True, help_text="연락처")
    privacy_agree = models.BooleanField(default=False, help_text="개인정보수집동의")
    child = models.OneToOneField(Child, on_delete=models.CASCADE, related_name="tester_child", null=True, blank=True, help_text="검사 아동")

    def __str__(self):
        return self.name + "(" + str(self.id) + ")"


class Answer(models.Model):
    child = models.OneToOneField(Child, on_delete=models.CASCADE, related_name="answer_child", null=True, blank=True, help_text="검사 아동")
    answers = ArrayField(models.IntegerField(), null=True, blank=True, help_text="제출답안 리스트")