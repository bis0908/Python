# -*- coding: utf-8 -*-
"""
step03_func_args

함수의 가변인수
- 한 개의 인수로 여러 개의 실인수를 받는 인수
형식) def 함수명 (인슈, *인수)

@author: wonseok
"""

# 1. 튜플형의 가변인수
def Func1(name, *names):
    print(name)
    print(names)

Func1('홍길동', '이순신', '강감찬')

def statis:



# dict형으로 받는 가변 인수
def person(h, w, **other):
    print('키 =', h)
    print('몸무게=', w)
    print('기타 =', other)

person(175, 68, name = '홍길동', age = '35')
'''
키 = 175
몸무게= 68
기타 = {'name': '홍길동', 'age': '35'}
'''

# 함수명을 인수로 받기
datas = [4, 2, 8]
datas * 0.5 # TypeError

# 각 변량에 곱셈 연산
def calc(x):
    return x * 0.5

def myfunc(calc, datas):
    re = [calc(x) for x in datas]
    return re

print(myfunc(calc, datas)) # [2.0, 1.0, 4.0]