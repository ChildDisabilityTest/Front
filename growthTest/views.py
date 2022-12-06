from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, "growthTest/home.html")

def userInfo(request):
    return render(request, "growthTest/userInfo.html")

def test(request):
    return render(request, "growthTest/test.html")

def result(request):
    return render(request, "growthTest/result.html")

def bar_chart(request):
    labels=["신체발달"]  # labels
    data=[43]           # 계산 값(점수)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })