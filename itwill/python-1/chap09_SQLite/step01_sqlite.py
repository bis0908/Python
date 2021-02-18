# -*- coding: utf-8 -*-
"""
step01_sqlite
 - 내장 DBMS: 기기 내부에서만 사용 가능한 DB
 - 외부 접근 허용 안됨

@author: wonseok
"""

import sqlite3

sqlite3.sqlite_version_info  # (3, 33, 0)

try:
    conn = sqlite3.connect('sqlite_db')  # create database

    # SQL 실행 객체 생성
    cursor = conn.cursor()

    # table 생성
    sql = '''create table if not exists test_tab(
                name text(10), age numeric(3), addr text(50))
            '''
    cursor.execute(sql)

    print('~~ Create table ~~')

    # add Record
    cursor.execute("insert into test_tab values('홍길동', 35, '한양')")
    cursor.execute("insert into test_tab values('이순신', 45, '해남')")
    cursor.execute("insert into test_tab values('강감찬', 55, '수원')")
    conn.commit()

    # Record 조회
    cursor.execute('select * from test_tab')
    dataset = cursor.fetchall()

    for row in dataset:
        print(row[0], row[1], row[2])  # tuple 형식

    # table 제거
    cursor.execute('drop table test_tab')
    print('~~ 테이블 삭제 완료 ~~')


except Exception as e:
    print('Err !!: ', e)
finally:
    cursor.close()
    conn.close()
