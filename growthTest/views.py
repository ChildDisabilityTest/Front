from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "growthTest/home.html")

@csrf_exempt
def test(request):
    if request.method == 'POST':
        # print("answer DB save")
        # a1 = request.POST.get('a1')
        # a2 = request.POST.get('a2')
        # a3 = request.POST.get('a3')
        # a4 = request.POST.get('a4')

        answer_list = [0]

        for i in range(1, 55):
            a = "a" + str(i)
            answer = request.POST.get(a)
            if answer is not None:
                answer = int(answer)
            answer_list.append(answer)

        print(answer_list)
        # print(answer_list[3])
        # print(answer_list[54])

        Answer.objects.create(
            child = 0,
            answers = answer_list
        )

        # print(a1,a2,a3,a4)

        return redirect('home')
    else:
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