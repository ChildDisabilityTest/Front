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
        childTerms = request.POST.get('childTerms')
        if childTerms == 'yes':
            privacy_agree = "True"
        else:
            privacy_agree = "False"

        # 지역 객체 가져오기
        residence = IncheonRegion.objects.get(id=country)

        # child 객체 만들기
        child = Child.objects.create(
            name = childName,
            birthDate = childBirthDate,
            kindergarden = kindergarden,
            residence = residence,
            gender = gender,
            privacy_agree = privacy_agree
        )

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
        # if not re.search(r'^01([0|1|6|7|8|9]?)?([0-9]{3,4})?([0-9]{4})$', (testerPhone)):
        #     print("invalid phone number")
        # else:
        #     print("valid phone number")

        # tester 객체 만들기 (<= 위에서 만든 child 1:1 연결)
        tester = Tester.objects.create(
            name = testerName,
            birthDate = testerBirthDate,
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
        emd = IncheonRegion.objects.all()
        return render(request, "user/userInfo.html", {'emd_list':emd})
