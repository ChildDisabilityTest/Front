import os
from .models import *
import pandas as pd

# 질문 업로드
def upload_questions():

    f_path = os.path.abspath(os.path.join(
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
        stage = "성숙",
        content = "현재 연령 수준에서 매우 적합하게 발달하고 있습니다. 일상에서 칭찬을 통해서 밝고 건강하게 자랄 수 있도록 해주세요."
    )
    Comment.objects.create(
        classification = "발달지수",
        stage = "보통",
        content = "현재 연령 수준에서 적합하게 발달하고 있습니다. 일상에서 보다 칭찬을 많이 해주셔서 밝고 건강하게 자랄 수 있도록 해주세요."
    )
    Comment.objects.create(
        classification = "발달지수",
        stage = "지연",
        content = "아동의 행동을 잘 관찰하시고, 관련한 전문가나 보다 세밀한 발달검사를 받아보실 것을 추천해 드립니다."
    )
    Comment.objects.create(
        classification = "자폐경향성",
        stage = "높음",
        content = "아동의 행동을 잘 관찰하시고, 관련한 전문가나 보다 세밀한 발달검사를 받아보실 것을 추천해 드립니다."
    )
    Comment.objects.create(
        classification = "자폐경향성",
        stage = "보통",
        content = "현재 연령 수준에서 적합하게 발달하고 있습니다. 일상에서 보다 칭찬을 많이 해주셔서 밝고 건강하게 자랄 수 있도록 해주세요."
    )
    Comment.objects.create(
        classification = "자폐경향성",
        stage = "낮음",
        content = "현재 연령 수준에서 매우 적합하게 발달하고 있습니다. 일상에서 보다 칭찬을 많이 해주셔서 밝고 건강하게 성장할 수 있도록 해주세요."
    )
    Comment.objects.create(
        classification = "ADHD경향성",
        stage = "높음",
        content = "아동의 행동을 잘 관찰하시고, 관련한 전문가나 보다 세밀한 발달검사를 받아보실 것을 추천해 드립니다."
    )
    Comment.objects.create(
        classification = "ADHD경향성",
        stage = "보통",
        content = "현재 연령 수준에서 적합하게 발달하고 있습니다. 일상에서 보다 칭찬을 많이 해주셔서 밝고 건강하게 자랄 수 있도록 해주세요."
    )
    Comment.objects.create(
        classification = "ADHD경향성",
        stage = "낮음",
        content = "현재 연령 수준에서 매우 적합하게 잘 발달하고 있습니다. 일상에서 칭찬을 많이 해주셔서 밝고 건강하게 자랄 수 있도록 해주세요."
    )
    print("!!comment upload success!!")
    return

# 규준표 업로드
def upload_criterion():

    f_path = os.path.abspath(os.path.join(
        '규준표.xlsx'
    ))

    df = pd.read_excel(f_path, engine='openpyxl', sheet_name=None)

    df1 = df['Sheet1']
    df2 = df['Sheet2']

    bulk_list = []

    for row in zip(df1['연령'], df1['원점수'], df1['백분위'], df1['T점수']):
        print(row)
        bulk_list.append(
            Criterion(
                column = '발달지수',
                age = int(row[0]),
                origin_score = int(row[1]),
                percentile = int(row[2]),
                T_score = int(row[3]),
                level = 'M' # 임시
            )
        )

    print("====")

    for row in zip(df2['원점수'], df2['ADHD 백분위'], df2['ADHD T점수'], df2['자폐 백분위'], df2['자폐 T점수']):
        print(row)
        bulk_list.append(
            Criterion(
                column = 'ADHD경향성',
                age = 0,
                origin_score = int(row[0]),
                percentile = int(row[1]),
                T_score = int(row[2]),
                level = 'M' # 임시
            )
        )
        bulk_list.append(
            Criterion(
                column = '자폐경향성',
                age = 0,
                origin_score = int(row[0]),
                percentile = int(row[3]),
                T_score = int(row[4]),
                level = 'M' # 임시
            )
        )

    C = Criterion.objects.bulk_create(bulk_list)

    print("!!criterion upload success!!")
    return