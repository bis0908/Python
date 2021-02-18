# -*- coding: utf-8 -*-
"""
step07_recursive.py

재귀호출
- 함수 내부에서 자신의 함수를 반복적으로 호출하는 기법
- 조건: 반드시 종료 되어야 함

@author: wonseok
"""

# 1. 카운터: 1 ~ n
def counter(n):
    if n == 0: # 종료 조건
        return 0
    else:
        counter(n-1) # 재귀호출: n = 5 -> : (4), (3), (2), (1)
        '''
        stack[5, 4, 3, 2, 1] -> Last In First Out
        '''
        print(n, end = ' ')

# 함수 호출
print('n = ', counter(10))

print()

# 2. 누적
def adder(n):
    if n == 1:
        return 1
    else:
        result = n + adder(n-1) # 재귀 호출 (n = 5 : 4, 3, 2)
        '''
        stack[5, 4, 3, 2] -> 1+|2+3+4+5+| = result
        '''
        print(result, end = ' ') # 3 6 10 15
        return result

print('n = ', adder(5))
