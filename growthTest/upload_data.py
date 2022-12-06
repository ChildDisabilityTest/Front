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
                content = l[3],
                test_column = l[2],
                group = l[1]
            )
        )
        
    Q = Question.objects.bulk_create(bulk_list)
    print("!!question upload success!!")
    return