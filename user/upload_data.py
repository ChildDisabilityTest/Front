import os, csv
from .models import *

"""
$ python manage.py shell
>>> from user.upload_data import *
>>> upload_region()
"""

# 지역정보 업로드
def upload_region():
    f_path = os.path.abspath(os.path.join(
        'region.csv'
    ))

    bulk_list = []

    with open(f_path, 'r', encoding='euc-kr') as f:
        reader = csv.reader(f)
        for row in reader:
            # print(row)
            bulk_list.append(
                Region(
                    name = row[0]
                )
            )

    R = Region.objects.bulk_create(bulk_list)
    print("!!Region upload success!!")
    return