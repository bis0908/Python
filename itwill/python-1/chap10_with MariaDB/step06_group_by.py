# -*- coding: utf-8 -*-
"""
step06_group_by

select * from table
group by 집단 변수(부서번호, 직책)
having 조건식;

@author: wonseok
"""


import pymysql

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

    # emp table: 부서번호 or 직책
    # gcol = int(input('그룹 칼럼 선택 (1. 부서, 2. 직책): '))
    # if gcol > 2 or gcol < 1:
    #     print('그룹 불가')
    # else:
    #     if gcol == 1:
    #         sql = '''select dno, sum(sal), avg(sal)
    #                  from emp
    #                  group by dno
    #                  order by dno '''
    #     else:
    #         sql = '''select job, sum(sal), avg(sal)
    #                  from emp
    #                  group by job '''

    # cursor.execute(sql)
    # data = cursor.fetchall()

    # for row in data:
    #     print(row[0], row[1], row[2])

    # Q. 부서별 급여 합계를 계산하여 합계가 300 이상인 부서만 출력
    sql = '''select dno, sum(sal), round(avg(sal), 2)
             from emp
             group by dno
             having sum(sal) >= 300'''
    cursor.execute(sql)
    data = cursor.fetchall()

    for row in data:
        print(row[0], row[1], row[2])

except Exception as e:
    print('db error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()
