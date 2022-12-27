from datetime import datetime
import math
from django.shortcuts import render, redirect
from .models import *
import re

# Create your views here.
def userInfo(request):
    # POST 요청 => 검사자/아동 정보 등록
    if request.method == 'POST':
        # 아동 정보 받아오기
        childName = request.POST.get('childName')
        childBirthDate = request.POST.get('childBirthDate')
        kindergarden = request.POST.get('kindergarden')
        country = request.POST.get('country')
        gender = request.POST.get('gender')

        # 지역 객체 가져오기
        residence = Region.objects.get(id=country)

        #* [error] 아동의 나이가 만 1세 미만 / 만 6세 초과일 경우 더이상 진행X
        birth_date = int(childBirthDate.replace('-', ''))
        now_date = int(datetime.now().date().strftime('%Y%m%d'))
        age = math.floor((now_date-birth_date)/10000)
        if age < 1 or age > 6:
            print("[ERROR] invalid child age")
            return redirect('home')

        # 검사자 정보 받아오기
        testerName = request.POST.get('testerName')
        testerBirthDate = request.POST.get('testerBirthDate')
        testerPhone = request.POST.get('testerPhone')
        testTerms = request.POST.get('testTerms')
        relationship = request.POST.get('relationship')
        if testTerms == 'yes':
            tester_privacy_agree = "True"
        else:
            tester_privacy_agree = "False"

        # 폰번호 형식 유효성 검사
        #* [error] 폰번호 형식이 유효하지 않으면 더이상 진행X
        if not re.search(r'^01([0|1|6|7|8|9]?)?([0-9]{3,4})?([0-9]{4})$', (testerPhone)):
            print("[ERROR] invalid phone number")
            return redirect('home')

        #! 입력된 정보가 모두 유효하면 child & tester 생성
        # child 객체 만들기
        child = Child.objects.create(
            name = childName,
            birthDate = childBirthDate,
            kindergarden = kindergarden,
            residence = residence,
            gender = gender,
            age = age
        )

        # tester 객체 만들기 (<= 위에서 만든 child 1:1 연결)
        if testerBirthDate:
            tester = Tester.objects.create(
                name = testerName,
                birthDate = testerBirthDate,
                phone_number = testerPhone,
                privacy_agree = tester_privacy_agree,
                child = child,
                relationship = relationship
            )
        else:
            tester = Tester.objects.create(
                name = testerName,
                phone_number = testerPhone,
                privacy_agree = tester_privacy_agree,
                child = child,
                relationship = relationship
            )

        # 검사자/아동 정보 처리 후 테스트 페이지로 리다이렉트 (쿠키에 child id 저장)
        response = redirect('test')
        response.set_cookie('child_id', child.id)
        return response

        
    # GET 요청 => 검사자/아동 정보 받는 템플릿 반환
    else:
        emd = Region.objects.all()
        return render(request, "user/userInfo.html", {'emd_list':emd})
