from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from datetime import datetime
import math
from user.models import *

def home(request):
    return render(request, "growthTest/home.html")

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

        # print(answer_list)

        # 쿠키에 저장된 검사 아동 id 가져오기 (-> child 객체 변환)
        child_id = request.COOKIES['child_id']
        child = Child.objects.get(pk=child_id)
        # print(child)

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
        questions = Question.objects.all().order_by('number')

        for i in range(0, questions.count(), chunk):
            questions_arr.append(questions[i:i+chunk])

        child_id = request.COOKIES['child_id']
        child = Child.objects.get(pk=child_id)
        tester = Tester.objects.get(child=child)
        # print(tester)
    
    return render(request, "growthTest/test.html", {'question_arr':questions_arr, 'tester':tester})

def result(request):
    # 결과 수치 계산 및 코멘트 반환
    child_id = request.COOKIES['child_id']
    child = Child.objects.get(pk=child_id)

    answer = Answer.objects.get(child=child)
    a = answer.answers
    r1 = 0 # 발달지수
    r2 = 0 # 자폐경향성
    r3 = 0 # ADHD경향성

    # 1번 ~ 30번 발달지수
    for i in range((child.age-1)*5+1, child.age*5+1):
        r1 += a[i]

    # 31번 ~ 42번 자폐경향성
    for i in range(31, 43):
        r2 += a[i]

    # 43번 ~ 54번 ADHD경향성
    for i in range(43, 55):
        r3 += a[i]

    print("====> ", r1,r2,r3)

    c1 = Criterion.objects.get(column="발달지수", age=child.age, origin_score=r1)
    c2 = Criterion.objects.get(column="자폐경향성", origin_score=r2)
    c3 = Criterion.objects.get(column="ADHD경향성", origin_score=r3)
    
    print("====> ", c1,c2,c3)

    print("--------------------")
    print("1. 발달지수")
    print("만 ", c1.age, "세")
    print("원점수 ", c1.origin_score, "점")
    print("백분위 ", c1.percentile, "%")
    print("T점수 ", c1.T_score, "점")
    print(c1.level)
    print("--------------------")
    print("2. 자폐경향성")
    print("원점수 ", c2.origin_score, "점")
    print("백분위 ", c2.percentile, "%")
    print("T점수 ", c2.T_score, "점")
    print(c2.level)
    print("--------------------")
    print("3. ADHD경향성")
    print("원점수 ", c3.origin_score, "점")
    print("백분위 ", c3.percentile, "%")
    print("T점수 ", c3.T_score, "점")
    print(c3.level)
    print("--------------------")

    comment1 = Comment.objects.get(classification="발달지수", level=c1.level)
    comment2 = Comment.objects.get(classification="자폐경향성", level=c2.level)
    comment3 = Comment.objects.get(classification="ADHD경향성", level=c3.level)
    print(comment1.stage, "-", comment1.content)
    print(comment2.stage, "-", comment2.content)
    print(comment3.stage, "-", comment3.content)

    Result.objects.create(
        child = child,
        development_origin_score = c1.origin_score,
        development_T_score = c1.T_score,
        development_percentile = c1.percentile,
        development_stage = comment1.stage,
        autism_origin_score = c2.origin_score,
        autism_T_score = c2.T_score,
        autism_percentile = c2.percentile,
        autism_stage = comment2.stage,
        adhd_origin_score = c3.origin_score,
        adhd_T_score = c3.T_score,
        adhd_percentile = c3.percentile,
        adhd_stage = comment3.stage
    )

    response = render(request, "growthTest/result.html", {'c1':c1,'c2':c2, 'c3':c3, 'comment1':comment1,'comment2':comment2, 'comment3':comment3})
    response.delete_cookie("child_id")

    return response
