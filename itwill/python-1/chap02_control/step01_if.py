# -*- coding: utf-8 -*-
"""
chap02_Control

step01_if.py

제어문 : 조건문(if) + 반복문(while, for)

R블럭 : {}
Python 블럭 : 콜론(:)과 들여쓰기(tab키)
"""

# 1. 조건문(if)

'''
형식1)
if 조건식 :
    실행문
    실행문
'''

var = 10

if var >= 50 : # 조건식 : 산술,관계,논리연산자
    print('var는 50보다 크다.')
    print('var =', var)

print('~~항상 실행~~')

#---------------------------------------------------------

'''
형식2)
if 조건식 :
    실행문 -> True
else :
    실행문 -> False
'''

if var >= 50 : # 조건식 : 산술,관계,논리연산자
    print('var는 50보다 크다.')
    print('var =', var)
else :
    print('var는 50보다 작다.')

# 시스템 시간/날짜 가져오기
import datetime # 모듈 가져오기

today = datetime.datetime.now() # 모듈.클래스.함수()
print(today) # 2021-01-29 10:39:43.112456

# object.member
day = today.weekday() # 요일 반환(0~6)
print(day) # 4

if day >= 5 :
    print('오늘은 주말')
else :
    print('오늘은 평일')


'''
형식3)
if 조건식1 :
    실행문1
elif 조건식2 :
    실행문2
else :
    실행문3
'''

# 키보드 입력 점수 : 100~85점 : '우수', 84~70 : '보통', 70미만 : '저조'
score = int(input('점수 입력(0~100) : '))

# 전역변수 : 특정 블럭에서 만든 변수 -> 블록 이후에서 사용 가능
if score >= 85 and score <= 100 :
    #print('우수')
    grade = '우수'
elif score >= 70 :
    #print('보통')
    grade = '보통'
else :
    #print('저조')
    grade = '저조'

# 블럭 이후
print("당신의 점수는 %d이고, 등급은 %s이다."%(score, grade))


# 블럭 if vs 한 줄 if

# 블럭 if
num = 9

if num >= 5 :
    result = num * 2
else :
    result = num + 2

print('result =', result) # result = 18


# 한 줄 if : 형식)  변수 = 참 if 조건식 else 거짓
result = num * 2 if num >= 5 else num + 2
print('result =', result)  # result = 18


# if + in : 형식) if 값 in data :
string = "홍길동이순신12344"

if '동' in string :
    print('동 문자 있음') # 동 문자 있음
else :
    print('동 문자 없음')
