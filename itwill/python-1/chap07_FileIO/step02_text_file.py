# -*- coding: utf-8 -*-
"""
step02_text_file.py

open('path/파일명', mode='r' or 'w' or 'a')
mode='r' : 파일 읽기 
mode='w' : 파일 쓰기 
mode='a' : 파일 쓰기 + 추가
"""


import os # file 경로, 디렉터리 변경 

# 절대경로 
os.chdir('C:\\ITWILL/3_Python-I/workspace/chap07_FileIO/data')

try :
    # 1. 파일 읽기 
    print('현재 경로 : ', os.getcwd())
    file = open('ftest.txt', mode='r') # file 객체 생성  
    print(file.read()) # file 전체 내용 > 출력 
    file.close() # file 객체 닫기    
    
    # 2. 파일 쓰기 : 자동 생성 
    file2 = open('ftest2.txt', mode='w') # file 객체 생성
    file2.write('my first text ~~~') # file 쓰기
    file2.close() # file 객체 닫기
    
    # 3. 파일 쓰기 : 내용 추가 
    file3 = open('ftest2.txt', mode='a') 
    file3.write('\nmy second text ~~~') # file 쓰기(추가)
    file3.close()
    
    '''
    file.read() : 전체 문서 읽기 
    file.readline() : 한 줄 읽기 
    file.readlines() : 줄 단위 전체 읽기 
    '''
    
    # 4. 줄 단위 읽기 
    print('줄 단위 읽기')
    file4 = open('ftest.txt', mode='r')
    line = file4.readline() # 한 줄 읽기 
    
    while line != "" :
        print(line) # 첫 줄 출력
        line = file4.readline() # 2번째 ~ end 
    file4.close()
    
    print('줄 단위 전체 읽기')
    file5 = open('ftest.txt', mode='r')
    lines = file5.readlines() # list
    print(lines)
    # ['programming is fun\n', 'very fun!\n', 'have a good time\n', 'mouse is input device\n', 'keyboard is input device\n', 'computer is input output system']
    print(type(lines), len(lines)) # <class 'list'> 6
    
    # 줄 단위 읽기 > 출력 
    for line in lines :
        # strip() : 문장 끝 불용어 제거(줄바꿈, 공백)
        print(line.strip()) # str.strip()
    
    # strip() 함수 예
    string = 'sfag12324\n \t \r'
    print('string :', string.strip()) # sfag12324
    
    file5.close()
    
    # with open('file', mode) as object :
    with open('ftest2.txt', mode='r') as rfile :
        lines = rfile.read()
        print(lines)
        # close() 생략 가능   
    with open('ftest3.txt', mode='w', encoding='utf-8') as wfile : 
        wfile.write('파이썬 파일 작성 연습')
        wfile.write('\n파이썬 파일 작성 연습2')    
        
    file6 = open('ftest3.txt', mode='r', encoding='utf-8') 
    print(file6.read())
    
except Exception as e:
    print('예외발생 : ', e)
finally :
    file6.close() # 객체 닫기 -> 종료 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
