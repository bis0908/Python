# -*- coding: utf-8 -*-
"""
step05_inner.py

중첩 함수
- 함수 안에 또 다른 함수 포함

def outer(인수):
    실행문
    def inner(인수)
        실행문
        return 'value'
    return 'value'

@author: wonseok
"""

# 1. 중첩 함수 예
def a():
    print('a 함수: Outer func')
    def b():
        print('b 함수: Inner func')
#    return b

# a 호출
b = a()
b()

# 중첩함수 응용
'''
외부함수 역할: data 생성, 내부함수 포함
내부함수 역할:data 연산/조작
'''

def outerfn(data):
    dataset = data # data 생성
    def tot():
        tot_val = sum(dataset) # data 연산
#        print('sum = ', tot_val)
        return tot_val

    def avg(tot_val):
        avg_val = tot_val / len(dataset)
        return avg_val
    return tot, avg

data = list(range(1, 101))

# outer 호출
tot, avg = outerfn(data)
# inner 호출
tot_val = tot()
print('sum = {0:,}'.format(tot_val))
avg_val = avg(tot_val)
print('avg = {0:.2f}'.format(avg_val))


# 3. nonlocal: inner -> outer 변수 수정(변경)
'''
getter(): 값을 외부로 반환 (획득)
setter(): 값을 외부에서 변경 (지정)
'''
def mainFn(num):
    num_val = num # data 생성

    def getter(): # 획득: 인수없고 return 있음
        return num_val

    def setter(value): # 지정자: 인수있고 return 없음
        nonlocal num_val
        num_val = value

    return getter, setter

gete, sete = mainFn(100)
print('num_val = ', gete())
sete(1000)
