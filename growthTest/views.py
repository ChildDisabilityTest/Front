from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "growthTest/home.html")

@csrf_exempt
def test(request):
    # POST 요청 => 답안 디비 저장
    if request.method == 'POST':

        answer_list = [0]

        # 답안 정보 받아오기
        for i in range(1, 55):
            a = "a" + str(i)
            answer = request.POST.get(a)
            if answer is not None:
                answer = int(answer)
            answer_list.append(answer)

        print(answer_list)

        # 쿠키에 저장된 검사 아동 id 가져오기 (-> child 객체 변환)
        child_id = request.COOKIES['child_id']
        child = Child.objects.get(pk=child_id)
        print(child)

        # Answer 객체 생성
        Answer.objects.create(
            child = child,
            answers = answer_list
        )

        return redirect('home')

    # GET 요청 => 테스트 페이지 반환
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