from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def userInfo(request):
    # POST 요청 => 검사자/아동 정보 등록
    if request.method == 'POST':
        print("========")
        name = request.POST.get('name')
        birthDate = request.POST.get('birthDate')
        kindergarden = request.POST.get('kindergarden')
        country = request.POST.get('country')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        # privacy_agree = request.POST.get('privacy_agree')
        privacy_agree = "True"
        print(name)
        print(country)
        residence = IncheonRegion.objects.get(id=country)
        Child.objects.create(
            name = name,
            birthDate = birthDate,
            kindergarden = kindergarden,
            residence = residence,
            # age = age,
            gender = gender,
            privacy_agree = privacy_agree
        )
        return redirect('home') # 임시 리다이렉트
    # GET 요청 => 검사자/아동 정보 받는 템플릿 반환
    else:
        emd = IncheonRegion.objects.all()
        return render(request, "user/userInfo.html", {'emd_list':emd})
