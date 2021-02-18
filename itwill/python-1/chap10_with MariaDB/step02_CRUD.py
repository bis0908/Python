# -*- coding: utf-8 -*-
"""
step02_CRUD.py

 CRUD
 - Create, Read Update, Delete
"""

import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'scott',
    'password': 'tiger',
    'database': 'work',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True}

try:
    # db 연동 객체 생성
    conn = pymysql.connect(**config)
    # sql문 실행 객체
    cursor = conn.cursor()

    # 2. 레코드 추가 : Create
    '''
    code = int(input('code input : '))
    name = input('name input : ')
    su = int(input('su input : '))
    dan = int(input('dan input : '))
    sql = f"insert into goods values({code},'{name}',{su},{dan})"
    cursor.execute(sql)
    conn.commit() # db 반영
    '''

    # 3. 레코드 수정 : Update : code -> su, dan 수정
    '''
    code = int(input('update code input : '))
    name = input('update name input : ')
    su = int(input('update su input : '))
    dan = int(input('update dan input : '))

    sql = f"""update goods set name='{name}', su={su}, dan={dan}
              where code={code}"""
    cursor.execute(sql)
    conn.commit() # db 반영
    '''

    # 4. 레코드 삭제 : Delete : code -> 삭제
    code = int(input('delete code input : '))
    sql = f"select * from goods where code = {code}"
    cursor.execute(sql)
    row = cursor.fetchone()

    if row:
        cursor.execute(f"delete from goods where code={code}")
        conn.commit()  # db 반영
    else:
        print('해당 code는 없습니다.')

    # 1. 레코드 조회 : Read
    cursor.execute("select * from goods")
    dataset = cursor.fetchall()  # 전체 레코드

    print('code\t name\t su\t dan')
    print('-'*40)
    for row in dataset:
        print("{0}      {1}     {2}    {3}".format(
            row[0], row[1], row[2], row[3]))

    print('-'*40)
    print('전체 레코드 수 : ', len(dataset))

    # slq문 작성
except Exception as e:
    print('db error :', e)
    conn.rollback()  # 이전 상태 리턴
finally:
    cursor.close()
    conn.close()
