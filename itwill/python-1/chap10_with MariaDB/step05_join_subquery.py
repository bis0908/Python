# -*- coding: utf-8 -*-
"""
step05_join_subquery



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

    # 1. ANSI inner join
    # sal = 200
    # sql = f'''select
    #             e.eno, e.ename, e.sal, d.dno
    #         from
    #             emp e
    #         inner join
    #             dept d on e.dno = d.dno and e.sal >= {sal} '''

    # cursor.execute(sql)
    # dataset = cursor.fetchall()

    # for row in dataset:
    #     print(row[0], row[1], row[2], row[3])

    # # 2. sub-query
    # dno = int(input('부서 번호 입력: '))
    # sql = f'''select eno, ename, job, dno
    #           from emp
    #           where dno = (select dno from dept where dno = {dno})'''

    # cursor.execute(sql)
    # data = cursor.fetchall()
    # if data:
    #     for row in data:
    #         print(row[0], row[1], row[2], row[3])
    # else:
    #     print('해당 Record 없음')

    # Q. sub-query: 사원의 이름(emp) -> 부서 정보(dept) 출력 or '해당 사원 없음'
    name = input('사원 이름 입력: ')
    sql = f'''select *
              from dept
              where dno = (select dno from emp where ename = '{name}')'''
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        for row in data:
            print(row)
    else:
        print('해당 사원 없음')

except Exception as e:
    print('db error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()