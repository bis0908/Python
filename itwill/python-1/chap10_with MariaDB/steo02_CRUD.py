# -*- coding: utf-8 -*-
"""
steo02_CRUD

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
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    cur.execute('select * from goods')
    dataset = cur.fetchall()

     # 5. 레코드 추가 : 2차(키보드 입력)

    code = int(input('code input : '))
    name = input('name input : ')
    qty = int(input('qty input : '))
    amount = int(input('amount input : '))
    # '{value}'
    sql = f"insert into goods values({code},'{name}',{qty},{amount})"
    cur.execute(sql)
    conn.commit()  # db 반영

    # 레코드 수정 : Update

    code = int(input('수정할 코드 입력 : '))  # 레코드 검색
    qty = int(input('수정할 수량 입력 : '))  # 레코드 수정
    amount = int(input('수정할 단가 입력 : '))  # 레코드 수정

    sql = f"update goods set qty={qty}, amount={amount} where code={code}"
    cur.execute(sql)
    conn.commit()  # db 반영

    # 레코드 삭제 : Delete
    '''
    문) 키보드로 삭제할 code를 입력받아서 해당 레코드를 삭제한다.
    delete from table명 where 조건식
    '''

    code = int(input('삭제할 코드 입력 : '))

    # 1) 해당 레코드 조회
    cur.execute(f"select * from goods where code = {code}")
    row = cur.fetchone()  # 검색 레코드 1개 경우

    # 해당 레코드 삭제
    if row:  # row != null
        sql = f"delete from goods where code = {code}"
        cur.execute(sql)
        conn.commit()  # db 반영
    else:
        print('해당 레코드 없음')

    # 전체 레코드 조회 : Read(Select)
    cur.execute('select * from goods')
    dataset = cur.fetchall()

    # 레코드 출력 : 양식문자 이용
    for row in dataset:
        print("%d    %s    %d    %5.2f" % (row))

    print('전체 레코드 수 : ', len(dataset))

    # 조건 검색 : 숫자(수량)
    '''
    sql = "select * from goods where qty >= 2"
    cursor.execute(sql)
    dataset = cursor.fetchall()'''

    # 레코드 출력
    for row in dataset:
        print("%d    %s    %d    %5.2f" % (row))

    print('전체 레코드 수 : ', len(dataset))

    # 조건 검색 : 문자열(상품명)
    name = input("검색할 상품명 입력 : ")
    sql = f"select * from goods where name like '%{name}%'"  # '%홍%'
    cur.execute(sql)
    dataset = cur.fetchall()




    print('code\t name\t qty\t amount')
    for row in dataset:
        print(row[0], row[1], row[2], row[3])

    print('Total record length: ', len(dataset))

except Exception as e:
    print('db error :', e)
    conn.rollback()

finally:
    cur.close()
    conn.close()