from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def home(request):
    return render(request, "growthTest/home.html")

# def userInfo(request):
#     return render(request, "growthTest/userInfo.html")

def test(request):
    questions = Question.objects.all()
    return render(request, "growthTest/test.html", {'question_list':questions})

def result(request):
    return render(request, "growthTest/result.html")

def bar_chart(request):
    labels=["신체발달"]  # labels
    data=[43]           # 계산 값(점수)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })