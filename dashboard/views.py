from django.shortcuts import redirect, render
from growthTest.models import *
import openpyxl
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
import os

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        print(request.user)
        r = Result.objects.all()
        return render(request, "dashboard/tables.html", {"result_list":r})
    else:
        return redirect('login')

def data_to_excel(request):
    if request.user.is_authenticated:
        df = pd.DataFrame(
            columns=['No.', '아동이름', '생년월일', '거주지역', '성별', '발달지수', '자폐경향성', 'ADHD경향성', '검사날짜']
        )
        result = Result.objects.all()
        for r in result:
            df = df.append(
                pd.DataFrame(
                    [[r.child.id, r.child.name, r.child.birthDate.strftime('%Y%m%d'), r.child.residence, r.child.gender, str(r.development_origin_score) + " (" + r.development_stage + ")", str(r.autism_origin_score) + " (" + r.autism_stage + ")", str(r.adhd_origin_score) + " (" + r.adhd_stage + ")", r.child.tested_at.strftime('%Y%m%d')]],
                    columns=['No.', '아동이름', '생년월일', '거주지역', '성별', '발달지수', '자폐경향성', 'ADHD경향성', '검사날짜']
                )
            )
        
        # print(df)
        df.to_excel('SOS_Lab_검사결과.xlsx', sheet_name='검사결과', index=False)

        file_root = os.path.abspath(os.path.join(
            "SOS_Lab_검사결과.xlsx"
        ))

        fs = FileSystemStorage(file_root)
        response = FileResponse(fs.open(file_root, 'rb'), filename="SOS_Lab_검사결과.xlsx")
        return response
    else:
        return redirect('login')