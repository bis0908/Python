# -*- coding: utf-8 -*-
"""
step07_csv_table

<작업순서>
1. table 생성
2. file read -> colummn 저장; 레코드 추가
3. 레코드 조회

@author: wonseok
"""


import pymysql
import pandas as pd # csv file read

path = 'E:\Code\Python\itwill\chap10_with MariaDB\data'

bmi = pd.read_csv(path + '\\bmi.csv')

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 20000 entries, 0 to 19999
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   height  20000 non-null  int64
#  1   weight  20000 non-null  int64
#  2   label   20000 non-null  object -> 집단 변수
# dtypes: int64(2), object(1)
# memory usage: 468.9+ KB
# None

height = bmi.height
weight = bmi.weight
label = bmi.label



config = {
    'host': '127.0.0.1',
    'user': 'scott',
    'password': 'tiger',
    'database': 'work',
    'port': 3307,
    'charset': 'utf8',
    'use_unicode': True}

try:
    # db 연동 객체
    conn = pymysql.connect(**config)
    # sql문 실행 객체
    cursor = conn.cursor()

    # 1. table 생성
    # sql = '''create or replace table bmi_tab(
    #             height int,
    #             weight int,
    #             label char(6) ) '''

    # cursor.execute(sql)
    # print('bmi 테이블 작성 완료')

    # 2. file read -> column
    # size = len(height)

    # for i in range(size):
    #     h = height[i]
    #     w = weight[i]
    #     l = label[i]
    #     sql = f"insert into bmi_tab values({h}, {w}, '{l}')"
    #     cursor.execute(sql)

    # conn.commit()

    # # 레코드 조회
    # cursor.execute('select * from bmi_tab')
    # data = cursor.fetchall()

    # for row in data:
    #     print(row[0], row[1], row[2])

    # print('전체 레코드 수 {0:} 개'.format(len(data)))

    # label 단위로 키와 몸무게 평균 계산 & 출력하기
    sql = '''select label, avg(height), avg(weight)
            from bmi_tab
            group by label'''
    cursor.execute(sql)
    data = cursor.fetchall()

    print('\n Label \t height \t weight')
    for row in data:
        print('{} {} {}'.format(row[0], row[1], row[2]))

    print('전체 레코드 수: {0:d}개'.format(len(data)))

except Exception as e:
    print('db error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()
