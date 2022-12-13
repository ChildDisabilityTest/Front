import os
from .models import *

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