from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def home(request):
    return render(request, "growthTest/home.html")

def test(request):
    questions = Question.objects.all()
    return render(request, "growthTest/test.html", {'question_list':questions})

def result(request):
    return render(request, "growthTest/result.html")

def bar_chart(request):
    labels=["신체발달", "a", "b", "c", "d", "e", "f"]  # labels
    data=[43, 60, 87, 69, 32, 12, 92]           # 계산 값(점수)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })