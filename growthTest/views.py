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

        return redirect('result')

    # GET 요청 => 테스트 페이지 반환
    else:
        questions_arr = []
        chunk = 5
        questions = Question.objects.all()

        for i in range(0, questions.count(), chunk):
            questions_arr.append(questions[i:i+chunk])
    
    return render(request, "growthTest/test.html", {'question_arr':questions_arr})

def result(request):
    # 결과 수치 계산 및 코멘트 반환
    #TODO 결과페이지에 보여줄 데이터 생성 (221208 작성)
    # 1. 쿠키에 있는 child_id 로 해당 아동의 답안(Answer) 불러와서 규준표 따라 계산
    # 2. 결과치 DB에 저장 후 (모델/필드 따로 만들어야 함)
    # 3. 그에 맞는 종합소견 코멘트 불러와서
    # 4. 수치/코멘트 한번에 같이 넘겨주기
    return render(request, "growthTest/result.html")

def bar_chart(request):
    # labels=["발달지수", "자폐경향성", "ADHD 경향성"]  # labels
    # data=[83, 35, 12]      # 계산 값(점수) 수정
    labels=[""]  
    data=[75]
    
    # 이런 식으로 계산 값만(라벨은 필요없음)
    return JsonResponse(data=[
        {'labels': labels, 'data': data,}, 
        {'labels': [""], 'data': [27],},
        {'labels': [""], 'data': [52],},
    ], safe=False)