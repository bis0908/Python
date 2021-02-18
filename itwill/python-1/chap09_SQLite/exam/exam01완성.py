'''
문제1) goods 테이블을 이용하여 다음과 같은 형식으로 출력하시오.
 <조건1> example 패키지에 db 파일 복사/붙여넣기 
 <조건2> HDTV 수량 수정 

    [ goods 테이블 현황 ]
1 냉장고 2 850000
2 세탁기 3 550000
3 전자레인지 5  600000
4 HDTV 2 1500000  
전체 레코드 수 : 4
'''

import sqlite3
import os 

os.chdir('C:/ITWILL/3_Python-I/workspace/chap09_SQLite') # db 생성 위치 

try:
    # db 연결 객체 생성 
    conn = sqlite3.connect('sqlite_db')
    # SQL 실행 객체 생성 
    cursor = conn.cursor()    
    
    # 1. 레코드 수정 
    sql = "update goods set su=2 where name='HDTV' "
    cursor.execute(sql) 
    sql = "update goods set su=5, dan=600000 where name='전자레인지' "
    cursor.execute(sql) 
    conn.commit() # db 반영 
    
    # 2. 전체 목록 보기
    sql = "select * from goods"
    cursor.execute(sql) # sql문 실행
    dataset = cursor.fetchall() # 전체 검색 
           
    # 레코드 출력 : 양식문자 
    for r in dataset : # fetchone()    
        print('%d    %s    %d     %d'%r)     
    
    print('전체 레코드 수 :', len(dataset))
        
# DB 연결 예외 처리          
except Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close() 
        
