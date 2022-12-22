from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
class IncheonRegion(models.Model):
    si = models.CharField(max_length=10, help_text="시")
    gu = models.CharField(max_length=10, help_text="구/군")
    emd = models.CharField(max_length=10, help_text="읍면동")

    def __str__(self):
        return self.si + " " + self.gu + " " + self.emd


class Child(models.Model):

    GENDER_CHOICES = (
        ('M', '남자'),
        ('F', '여자')
    )

    name = models.CharField(max_length=10, help_text="이름")
    birthDate = models.DateField(help_text="생년월일")
    residence = models.ForeignKey(IncheonRegion, on_delete=models.CASCADE, related_name="residence", help_text="거주지역")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, help_text="성별")
    kindergarden = models.CharField(max_length=20, null=True, blank=True, help_text="유치원 이름")
    privacy_agree = models.BooleanField(default=False, help_text="개인정보수집동의")
    tested_at = models.DateField(auto_now_add=True, help_text="검사일")

    def __str__(self):
        return self.name + "(" + str(self.id) + ")"


class Tester(models.Model):

    RELATIONSHIP_CHOICES = (
        ('F', '부'),
        ('M', '모'),
        ('G', '조부모'),
        ('T', '교사'),
        ('E', '기타'),
    )

    name = models.CharField(max_length=10, help_text="이름")
    birthDate = models.DateField(null=True, blank=True, help_text="생년월일")
    phone_number = models.CharField(max_length = 11, help_text="연락처")
    privacy_agree = models.BooleanField(default=False, help_text="개인정보수집동의")
    child = models.OneToOneField(Child, on_delete=models.CASCADE, related_name="tester_child", help_text="검사 아동")
    relationship = models.CharField(max_length=1, choices=RELATIONSHIP_CHOICES, help_text="아동과의 관계")

    def __str__(self):
        return self.name + "(" + str(self.id) + ")"