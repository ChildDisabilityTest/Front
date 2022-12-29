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
            columns=[
                'No.', 
                '이름', 
                '생년월일', 
                '만나이',
                '거주지역', 
                '성별',
                '어린이집/유치원 이름',
                '발달지수 (원점수)', 
                '발달지수 (T점수)', 
                '발달지수 (백분위)', 
                '발달지수 (단계)', 
                '자폐경향성 (원점수)', 
                '자폐경향성 (T점수)', 
                '자폐경향성 (백분위)', 
                '자폐경향성 (단계)', 
                'ADHD경향성 (원점수)', 
                'ADHD경향성 (T점수)', 
                'ADHD경향성 (백분위)', 
                'ADHD경향성 (단계)', 
                '검사날짜',
                '1','2','3','4','5','6','7','8','9','10',
                '11','12','13','14','15','16','17','18','19','20',
                '21','22','23','24','25','26','27','28','29','30',
                '31','32','33','34','35','36','37','38','39','40',
                '41','42','43','44','45','46','47','48','49','50',
                '51','52','53','54',
                '검사자 이름',
                '검사자 생년월일',
                '검사자 휴대폰번호',
                '검사자 아동과의 관계',
                '검사자 개인정보동의여부',
            ]
        )
        result = Result.objects.all()
        for r in result:
            a = r.child.answer_child.answers
            df = df.append(
                pd.DataFrame(
                    [[
                        r.child.id, # No.
                        r.child.name, # 이름
                        r.child.birthDate.strftime('%Y-%m-%d'), # 생년월일
                        r.child.age, # 만나이
                        r.child.residence, # 거주지역
                        r.child.get_gender_display(), #성별
                        r.child.kindergarden, # 어린이집/유치원 이름
                        r.development_origin_score, # 발달지수 원점수
                        r.development_T_score, # 발달지수 T점수
                        r.development_percentile, # 발달지수 백분위
                        r.development_stage, # 발달지수 단계
                        r.autism_origin_score, # 자폐경향성 원점수
                        r.autism_T_score, # 자폐경향성 T점수
                        r.autism_percentile, # 자폐경향성 백분위
                        r.autism_stage, # 자폐경향성 단계
                        r.adhd_origin_score, # ADHD경향성 원점수
                        r.adhd_T_score, # ADHD경향성 T점수
                        r.adhd_percentile, # ADHD경향성 백분위
                        r.adhd_stage, # ADHD경향성 단계
                        r.child.tested_at.strftime('%Y-%m-%d'), # 검사날짜
                        a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],
                        a[11],a[12],a[13],a[14],a[15],a[16],a[17],a[18],a[19],a[20],
                        a[21],a[22],a[23],a[24],a[25],a[26],a[27],a[28],a[29],a[30],
                        a[31],a[32],a[33],a[34],a[35],a[36],a[37],a[38],a[39],a[40],
                        a[41],a[42],a[43],a[44],a[45],a[46],a[47],a[48],a[49],a[50],
                        a[51],a[52],a[53],a[54],
                        r.child.tester_child.name, # 검사자 이름
                        r.child.tester_child.birthDate, # 검사자 생년월일
                        r.child.tester_child.phone_number, # 검사자 휴대폰번호
                        r.child.tester_child.get_relationship_display(), # 검사자 아동과의관계
                        r.child.tester_child.privacy_agree, # 검사자 개인정보동의여부
                    ]],
                    columns=[
                        'No.', 
                        '이름', 
                        '생년월일', 
                        '만나이',
                        '거주지역', 
                        '성별',
                        '어린이집/유치원 이름',
                        '발달지수 (원점수)', 
                        '발달지수 (T점수)', 
                        '발달지수 (백분위)', 
                        '발달지수 (단계)', 
                        '자폐경향성 (원점수)', 
                        '자폐경향성 (T점수)', 
                        '자폐경향성 (백분위)', 
                        '자폐경향성 (단계)', 
                        'ADHD경향성 (원점수)', 
                        'ADHD경향성 (T점수)', 
                        'ADHD경향성 (백분위)', 
                        'ADHD경향성 (단계)', 
                        '검사날짜',
                        '1','2','3','4','5','6','7','8','9','10',
                        '11','12','13','14','15','16','17','18','19','20',
                        '21','22','23','24','25','26','27','28','29','30',
                        '31','32','33','34','35','36','37','38','39','40',
                        '41','42','43','44','45','46','47','48','49','50',
                        '51','52','53','54',
                        '검사자 이름',
                        '검사자 생년월일',
                        '검사자 휴대폰번호',
                        '검사자 아동과의 관계',
                        '검사자 개인정보동의여부',
                    ]
                )
            )
        
        # print(df)
        df.to_excel('SOS_Lab_검사결과.xlsx', sheet_name='검사결과', index=False)

        file_root = os.path.abspath(os.path.join(
            "SOS_Lab_검사결과.xlsx"
        ))

        wb = openpyxl.load_workbook(file_root)
        ws = wb.active

        # 열너비 조정
        ws.column_dimensions["C"].width = 11 # 생년월일
        ws.column_dimensions["E"].width = 17 # 거주지역
        ws.column_dimensions["G"].width = 14 # 어린이집/유치원이름
        ws.column_dimensions["T"].width = 11 # 검사날짜
        ws.column_dimensions["U"].width = 3 # 답안
        ws.column_dimensions["BX"].width = 11 # 검사자 생년월일
        ws.column_dimensions["BY"].width = 13 # 검사자 휴대폰번호

        for col in range(21,75):
            ws.column_dimensions[openpyxl.utils.get_column_letter(col)].width = 4 # 답안

        # 가운데 정렬
        for row in ws.rows:
            for cell in row:
                cell.alignment = openpyxl.styles.Alignment(horizontal="center", vertical="center", wrap_text=True)

        wb.save('SOS_Lab_검사결과.xlsx')

        fs = FileSystemStorage(file_root)
        response = FileResponse(fs.open(file_root, 'rb'), filename="SOS_Lab_검사결과.xlsx")
        return response
    else:
        return redirect('login')