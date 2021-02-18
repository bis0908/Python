# -*- coding: utf-8 -*-
"""
step01_func_basic



@author: wonseok
"""

# 사용자 정의 함수
def userFn1():
    print('userFn1')

userFn1()

def userFn2(x, y):
    print('userFn2')
    z = x + y
    print('z:', z)

userFn2(10, 200)

def userFn3(x, y):
    print('userFn3')
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return add, sub, mul, div

userFn3(3, 5)

a, s, m, d = userFn3(10, 20)
print('add=', a)
print('sub=', s)
print('mul=', m)
print('div=', d)

calc = userFn3(10, 20)
print(calc, type(calc), calc[0])

# 실인수: 키보드 입력
x = int(input('x input: '))
y = int(input('y input: '))
calc = userFn3(x, y)
print('calc =', calc)



# Library 함수
'''
built-in 함수: 내장 함수
import 함수: import 'module name' or import 'package.module''
'''

# built-in: 내장 함수
dataset = [1, 2, 3, 4, 5]
print('sum =', sum(dataset))
print('max =', max(dataset))

# import 함수
import statistics
from statistics import mean, median
print('mean =', statistics.mean(dataset))
print('median =', median(dataset))

# 모듈 정보 제공
dir(statistics)
