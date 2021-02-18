# -*- coding: utf-8 -*-
"""
step04_emp_table

1. Table 유무 판단: show tables;
 -> Table 없음: Table 생성 및 레코드 추가
 -> Table 있음: 레코드 조회

2. 기본 키 자동번호 생성

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

   # 1. Table 유무 판단
    cursor.execute('show tables')
    tables = cursor.fetchall()
    print(tables) # (('goods',), ('zipcode_tab',)) -> 중첩 tuple

    sw = False
    for table in tables:
        if 'emp' in table:
            sw = True

    if sw:  # table 있는 경우
        sql = 'select * from emp'
        cursor.execute(sql)
        dataset = cursor.fetchall()

        for row in dataset:
            print(row[0], row[1], row[5], row[6])

    else:   # table 없는 경우
        sql = '''
                create table emp(
                    eno int auto_increment primary key,
                    ename varchar(20) not null,
                    hiredate date not null,
                    sal int not null,
                    bonus int default 0,
                    job varchar(20) not null,
                    dno int ) '''
        cursor.execute(sql)
        print('emp table 생성!')

        sql2 = 'alter table emp auto_increment = 1001'
        cursor.execute(sql2)

        # 레코드 추가
        sql3 = '''insert into emp(ename, hiredate, sal, bonus, job, dno)
                    values('홍길동', '2008-10-20', 300, 35, '관리자', 10)'''
        cursor.execute(sql3)

        sql3 = '''insert into emp(ename, hiredate, sal, job, dno)
                    values('강호동', '2010-10-20', 250, '사원', 20)'''
        cursor.execute(sql3)

        sql3 = '''insert into emp(ename, hiredate, sal, job, dno)
                    values('홍길동', '2008-03-20', 200, '사원', 10)'''
        cursor.execute(sql3)
        conn.commit()

        print('emp 테이블 레코드 추가 완료!!')

except Exception as e:
    print('db error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()
