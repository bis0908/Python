# -*- coding: utf-8 -*-
"""
step03_zipcode_table

text file -> DB 저장
1. table 생성
2. zipcode.txt -> 서울 지역 -> 레코드 추가
3. table -> 레코드 조회(동으로 검색)

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

    # 1. table 생성
    # sql = '''
    #     create table zipcode_tab(
    #         code char(14) not null,
    #         city varchar(15) not null,
    #         gu varchar(20) not null,
    #         dong varchar(60) not null,
    #         detail varchar(50)
    #         ) '''

    # cursor.execute(sql) # 쿼리문 날리기
    # print('1. zipcode table 생성 완료')

    # 2. 레코드 추가 or 조회
    cursor.execute('select * from zipcode_tab')
    dataset = cursor.fetchall()

    if dataset: # 레코드 있음
        # 레코드 조회
        choice = int(input('1. 동 검색, 2. 구 검색: '))
        if choice == 1:
            dong = input('검색할 동 입력: ')
            sql = f"select * from zipcode_tab where dong like '%{dong}%'"
            cursor.execute(sql)
            dataset = cursor.fetchall()
            for row in dataset:
                print(row[0], row[1], row[2], row[3], row[4])

            print('검색된 레코드: ', len(dataset))

        elif choice == 2:
            gu = input('검색할 구 입력: ')
            sql = f"select * from zipcode_tab where gu like '%{gu}%'"
            cursor.execute(sql)
            dataset = cursor.fetchall()
            for row in dataset:
                print(row[0], row[1], row[2], row[3], row[4])

            print('검색된 레코드: ', len(dataset))

        else:
            print('해당 번호는 없습니다.')

    else:   # 레코드 없음
        file = open('E:\Code\Python\itwill\chap10_with MariaDB\data\zipcode.txt', encoding = 'utf-8')
        line = file.readline()

        while line:
            token = line.split('\t') # token
            if token[1] == '서울':
                code = str(token[0]); city = token[1]
                gu = token[2]; dong = token[3]
                detail = token[4] # 있거나 없거나
                if detail: # 상세 주소 있음
                    sql = f'''insert into zipcode_tab values(
                                '{code}', '{city}', '{gu}', '{dong}', '{detail}' )'''
                else:   # 상세 주소 없음
                    sql = f'''insert into zipcode_tab(code, city, gu, dong) values(
                                '{code}', '{city}', '{gu}', '{dong}' )'''

                cursor.execute(sql)
                conn.commit()
            line = file.readline() # 2줄 ~ 마지막 줄

        file.close() # file object 닫기
        print('2. Record 추가 성공')




except Exception as e:
    print('db error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()