# -*- coding: utf-8 -*-
"""
step04_lambda_scope.py
1. 축약 함수

@author: wonseok
"""

# 1. 축약함수
'''
형식) 변수 = lambda 인수: 리터값
ex) lambda x, y = x + y
'''

# 일반 함수
def addr(x, y):
    add = x + y
    return add

print('add =', addr(10, 20))

# 람다 함수
addr2 = lambda x, y : x + y
print('add =', addr2(10, 20))

# x 변량에 제곱
dataset = [2, 4, 2.5, 3, 2, 5, 3.5, 6]
len(dataset)

square = lambda x : [d ** 2 for d in dataset] # list + for
print('square =', square(dataset)) # [4, 16, 6.25, 9, 4, 25, 12.25, 36]

# 혈액형 dummy 변수: ab(1), a, b, o(0)
dt = {'a': 0, 'b': 0, 'ab': 1, 'o': 0} # dict

dummy = lambda x : []


# 2. scope: 변수 사용 범위
'''
- 전역 변수: 전체 모듈에서 사용
- 지역 변수: 특정 블록(함수)에서 사용
'''


x = 50

def localFunc(x):
    x += 50 # x = x + 50
    return x # -> 100 지역변수; 호출 종료되면 소멸

localFunc(x) # 100
print(x) # 50

# 함수 내에서 전역 변수 사용
def globalFunc():
    global x
    x += 50

globalFunc()
print(x) # 100
