# -*- coding: utf-8 -*-
"""
step02_CRUD.py

CRUD
 - Create(Insert), Read(Select), Update, Delete
"""

import sqlite3  # db 생성 & db 연동
import os

os.chdir('E:\Code\Python\itwill\chap09_SQLite')  # db 생성 위치

try:
    # db 연동 객체 생성
    conn = sqlite3.connect('sqlite_db')
    # SQL문 실행 객체 생성
    cursor = conn.cursor()

    # 1. table 생성
    sql = """create table if not exists goods(
    code integer primary key,
    name text(30) unique not null,
    qty integer default 0,
    amount real default 0.0)"""
    cursor.execute(sql)  # 실제 table 생성
    print('table 생성 성공')

    # 2. 레코드 추가 : Create(Insert)

    # cursor.execute("insert into goods values(1, '냉장고', 2, 850000)")
    # cursor.execute("insert into goods values(2, '세탁기', 3, 550000)")
    # cursor.execute("insert into goods(code,name) values(3,'전자레인지')")
    # cursor.execute("insert into goods(code,name,amount) values(4,'HDTV',1500000)")
    # conn.commit() # db 반영

    # 5. 레코드 추가 : 2차(키보드 입력)

    code = int(input('code input : '))
    name = input('name input : ')
    qty = int(input('qty input : '))
    amount = int(input('amount input : '))
    # '{value}'
    sql = f"insert into goods values({code},'{name}',{qty},{amount})"
    cursor.execute(sql)
    conn.commit()  # db 반영

    # 6. 레코드 수정 : Update

    code = int(input('수정할 코드 입력 : '))  # 레코드 검색
    qty = int(input('수정할 수량 입력 : '))  # 레코드 수정
    amount = int(input('수정할 단가 입력 : '))  # 레코드 수정

    sql = f"update goods set qty={qty}, amount={amount} where code={code}"
    cursor.execute(sql)
    conn.commit()  # db 반영

    # 7. 레코드 삭제 : Delete
    '''
    문) 키보드로 삭제할 code를 입력받아서 해당 레코드를 삭제한다.
    delete from table명 where 조건식
    '''

    code = int(input('삭제할 코드 입력 : '))

    # 1) 해당 레코드 조회
    cursor.execute(f"select * from goods where code = {code}")
    row = cursor.fetchone()  # 검색 레코드 1개 경우

    # 1) 해당 레코드 삭제
    if row:  # row != null
        sql = f"delete from goods where code = {code}"
        cursor.execute(sql)
        conn.commit()  # db 반영
    else:
        print('해당 레코드 없음')

    # 3. 전체 레코드 조회 : Read(Select)
    cursor.execute('select * from goods')
    dataset = cursor.fetchall()

    # 레코드 출력 : 양식문자 이용
    for row in dataset:
        print("%d    %s    %d    %5.2f" % (row))

    print('전체 레코드 수 : ', len(dataset))

    # 4. 조건 검색 : 숫자(수량)
    '''
    sql = "select * from goods where qty >= 2"
    cursor.execute(sql)
    dataset = cursor.fetchall()'''

    # 레코드 출력
    for row in dataset:
        print("%d    %s    %d    %5.2f" % (row))

    print('전체 레코드 수 : ', len(dataset))

    # 4. 조건 검색 : 문자열(상품명)
    name = input("검색할 상품명 입력 : ")
    sql = f"select * from goods where name like '%{name}%'"  # '%홍%'
    cursor.execute(sql)
    dataset = cursor.fetchall()

    if dataset:
        for row in dataset:
            print(row[0], row[1], row[2], row[3])
    else:
        print('해당 상품명은 없습니다.')

except Exception as e:
    print('db error :', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
