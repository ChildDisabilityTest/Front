from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def home(request):
    return render(request, "growthTest/home.html")

def test(request):
    questions_arr = []
    chunk = 5
    questions = Question.objects.all()

    for i in range(0, questions.count(), chunk):
        questions_arr.append(questions[i:i+chunk])
    
    return render(request, "growthTest/test.html", {'question_arr':questions_arr})

def result(request):
    return render(request, "growthTest/result.html")

def bar_chart(request):
    # labels=["발달지수", "자폐경향성", "ADHD 경향성"]  # labels
    # data=[83, 35, 12]      # 계산 값(점수) 수정
    labels=[""]     # 라벨링은 따로,,,,?
    data=[75]
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })