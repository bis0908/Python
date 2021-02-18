# -*- coding: utf-8 -*-
"""
step01_try.py

예외처리 : run time error 처리 
 - file/DB 입출시 사용

형식)
try :
    예외발생 코드
except :
    예외처리 코드 
finally : -> 생략 가능 
    항상 실행 코드    
"""

x = [10, 30, 10.5, 'num', 7]

for i in x :
    print('i=', i)
    try :
        file = open('c:/text.txt') # file 열기 
        y = i**2 # 사칙연산 
        print('y=', y)
    except Exception as e:
        print('예외정보 : ', e) # 예외처리 
        

















