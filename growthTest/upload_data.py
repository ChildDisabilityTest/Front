import os
from .models import *
import pandas as pd

"""
$ python manage.py shell
>>> from growthTest.upload_data import *
>>> upload_questions()
>>> upload_comments()
>>> upload_criterion()
"""

# 질문 업로드
def upload_questions():

    f_path = os.path.abspath(os.path.join(
        'data',
        'question.txt'
    ))

    bulk_list = []

    f = open(f_path, 'r', encoding='UTF-8')
    while True:
        line = f.readline()
        if not line: break
        # print(line)
        l = line.strip().split('|')
        bulk_list.append(
            Question(
                number = int(l[0]),
                content = l[1],
                column = l[2],
                age = int(l[3])
            )
        )
        
    Q = Question.objects.bulk_create(bulk_list)
    print("!!question upload success!!")
    return

# 종합소견 코멘트 업로드
def upload_comments():
    Comment.objects.create(
        classification = "발달지수",
        level = "H",
        stage = "성숙",
        content = "현재 연령 수준에서 매우 적합하게 발달하고 있습니다. 일상에서 칭찬을 통해서 밝고 건강하게 자랄 수 있도록 해주세요."
    )
    Comment.objects.create(
        classification = "발달지수",
        level = "M",
        stage = "보통",
        content = "현재 연령 수준에서 적합하게 발달하고 있습니다. 일상에서 보다 칭찬을 많이 해주셔서 밝고 건강하게 자랄 수 있도록 해주세요."
    )
    Comment.objects.create(
        classification = "발달지수",
        level = "L",
        stage = "지연",
        content = "아동의 행동을 잘 관찰하시고, 관련한 전문가나 보다 세밀한 발달검사를 받아보실 것을 추천해 드립니다."
    )
    Comment.objects.create(
        classification = "자폐경향성",
        level = "H",
        stage = "높음",
        content = "아동의 행동을 잘 관찰하시고, 관련한 전문가나 보다 세밀한 발달검사를 받아보실 것을 추천해 드립니다."
    )
    Comment.objects.create(
        classification = "자폐경향성",
        level = "M",
        stage = "보통",
        content = "현재 연령 수준에서 적합하게 발달하고 있습니다. 일상에서 보다 칭찬을 많이 해주셔서 밝고 건강하게 자랄 수 있도록 해주세요."
    )
    Comment.objects.create(
        classification = "자폐경향성",
        level = "L",
        stage = "낮음",
        content = "현재 연령 수준에서 매우 적합하게 발달하고 있습니다. 일상에서 보다 칭찬을 많이 해주셔서 밝고 건강하게 성장할 수 있도록 해주세요."
    )
    Comment.objects.create(
        classification = "ADHD경향성",
        level = "H",
        stage = "높음",
        content = "아동의 행동을 잘 관찰하시고, 관련한 전문가나 보다 세밀한 발달검사를 받아보실 것을 추천해 드립니다."
    )
    Comment.objects.create(
        classification = "ADHD경향성",
        level = "M",
        stage = "보통",
        content = "현재 연령 수준에서 적합하게 발달하고 있습니다. 일상에서 보다 칭찬을 많이 해주셔서 밝고 건강하게 자랄 수 있도록 해주세요."
    )
    Comment.objects.create(
        classification = "ADHD경향성",
        level = "L",
        stage = "낮음",
        content = "현재 연령 수준에서 매우 적합하게 잘 발달하고 있습니다. 일상에서 칭찬을 많이 해주셔서 밝고 건강하게 자랄 수 있도록 해주세요."
    )
    print("!!comment upload success!!")
    return

# 규준표 업로드
def upload_criterion():

    f_path = os.path.abspath(os.path.join(
        'data',
        '규준표.xlsx'
    ))

    df = pd.read_excel(f_path, engine='openpyxl', sheet_name=None)

    df1 = df['Sheet1']
    df2 = df['Sheet2']

    bulk_list = []

    for row in zip(df1['연령'], df1['원점수'], df1['백분위'], df1['T점수']):
        # print(row)
        if int(row[3]) <= 40:
            level = 'L'
        elif int(row[3]) >= 60:
            level = 'H'
        else:
            level = 'M'
        bulk_list.append(
            Criterion(
                column = '발달지수',
                age = int(row[0]),
                origin_score = int(row[1]),
                percentile = int(row[2]),
                T_score = int(row[3]),
                level = level
            )
        )


    for row in zip(df2['원점수'], df2['ADHD 백분위'], df2['ADHD T점수'], df2['자폐 백분위'], df2['자폐 T점수']):
        # print(row)
        if int(row[2]) <= 40:
            level1 = 'L'
        elif int(row[2]) >= 60:
            level1 = 'H'
        else:
            level1 = 'M'

        if int(row[4]) <= 40:
            level2 = 'L'
        elif int(row[4]) >= 60:
            level2 = 'H'
        else:
            level2 = 'M'
        bulk_list.append(
            Criterion(
                column = 'ADHD경향성',
                age = 0,
                origin_score = int(row[0]),
                percentile = int(row[1]),
                T_score = int(row[2]),
                level = level1
            )
        )
        bulk_list.append(
            Criterion(
                column = '자폐경향성',
                age = 0,
                origin_score = int(row[0]),
                percentile = int(row[3]),
                T_score = int(row[4]),
                level = level2
            )
        )

    C = Criterion.objects.bulk_create(bulk_list)

    print("!!criterion upload success!!")
    return