from django.shortcuts import render, redirect
from .models import *

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
        privacy_agree = "True"

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
        testerPhone = request.POST.get('testerPhone') # ex) +821012341234 (country_code=82, national_number=1012341234)
        tester_privacy_agree = "True"

        # tester 객체 만들기 (<= 위에서 만든 child 1:1 연결)
        tester = Tester.objects.create(
            name = testerName,
            birthDate = testerBirthDate,
            phone_number = testerPhone,
            privacy_agree = tester_privacy_agree,
            child = child
        )

        return redirect('home') # 임시 리다이렉트
    # GET 요청 => 검사자/아동 정보 받는 템플릿 반환
    else:
        emd = IncheonRegion.objects.all()
        return render(request, "user/userInfo.html", {'emd_list':emd})
