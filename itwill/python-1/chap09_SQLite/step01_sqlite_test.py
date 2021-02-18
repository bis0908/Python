# -*- coding: utf-8 -*-
"""
step01_sqlite_test.py

sqlite3 
 - 내장 DBMS : 기기 내부에서만 사용가능한 DB
 - 외부 접근 허용 안됨 
"""

import sqlite3
import os 

os.chdir('C:/ITWILL/3_Python-I/workspace/chap09_SQLite') # db 생성 위치 

print(sqlite3.sqlite_version_info) # (3, 33, 0)

try :
    # db 생성 & 연동 객체 생성  
    conn = sqlite3.connect('sqlite_db') # 1. db 생성 
    #print('~~ db 생성 ~~')  
    # SQL문 실행 객체 생성 
    cursor = conn.cursor()      
    
    # 2. table 생성 
    sql = """create table if not exists test_tab(
             name text(10), age numeric(3), addr text(50))"""
    
    cursor.execute(sql) # 실제 table 생성 : # auto commit 
    #print('~~ table 생성 ~~')
    
    # 3. 레코드 추가     
    cursor.execute("insert into test_tab values('홍길동',35,'한양')")
    cursor.execute("insert into test_tab values('이순신',45,'해남')")
    cursor.execute("insert into test_tab values('강감찬',55,'평양')")
    conn.commit() # db 반영 
        
    # 4. 레코드 조회 
    cursor.execute('select * from test_tab')
    dataset = cursor.fetchall() # 레코드 3개 가져오기 
    
    # 레코드 단위 출력 
    for row in dataset : 
        #print(row) # tuple 형식
        print(row[0], row[1], row[2]) # 칼럼 단위 분리   
    
    # 5. table 제거 
    cursor.execute('drop table test_tab') # auto commit 
    print('~~ table 삭제 ~~')
    
except Exception as e:
    print('db 연동 오류 : ', e)
finally :
    cursor.close(); conn.close() # 객체 닫기 











