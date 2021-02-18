# -*- coding: utf-8 -*-
"""
step01_class_basic.py

클래스(class)?
 - 관련 있는 함수와 자료를 묶어서 객체 생성 역할
 - 구성요소 : 메서드(함수) + 속성(변수) + 생성자(객체 생성)
 - 멤버 : 메서드(자료 처리) + 속성(자료 저장)
 - 유형 : 사용자정의 클래스, 라이브러리 클래스

형식)
class 클래스명 :
    속성 = 자료
    생성자 : 객체 생성
    def 메서드() :
        속성 처리
"""

# 1. 중첩함수 vs 클래스

# 1) 중첩함수
def calcFn(a, b) : # outer 함수 : data 저장
    # data 생성
    x = a # 10
    y = b # 20

    # inner 함수 :  data 연산
    def plus():
        z = x + y # data 연산
        return z
    def minus() :
        z = x - y # data 연산
        return z

    return plus, minus


#outer 함수 호출
plus, minus = calcFn(10, 20)
# inner 함수 호출
print('plus =', plus()) # plus = 30
print('minus =', minus()) # minus = -10


# 2) 클래스 : 중첩함수 -> 클래스
class calcClass : # outer -> 클래스
    # 1.속성(전역변수) : data 저장
    x = 0 # 10
    y = 0 # 20

    '''
    self : 기본인수 -> 멤버(메서드+속성) 호출
    '''
    # 2.생성자(함수) # 객체 생성 + 속성 초기화
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    # 3.메서드(함수) :  inner -> 메서드
    def plus(self):
        z = self.x + self.y # data 연산
        return z
    def minus(self):
        z = self.x - self.y # data 연산
        return z

# 객체 생성
obj = calcClass(10, 20) # 생성자 -> 객체 생성

# 객체.메서드()
print('plus =', obj.plus()) # plus = 30
print('minus =', obj.minus()) # minus = -10

# 멤버 확인 : 메서드, 속성
dir(obj) # 'minus','plus','x','y'

# 객체.속성
print('x =', obj.x) # x = 10
print('y =', obj.y) # y = 20

# 객체 출처
print(type(obj)) # <class '__main__.calcClass'>


# class(1) vs object(n)
obj2 = calcClass(100, 200)

print(obj2.plus()) # 300
print(obj2.minus()) # -100
print(type(obj2)) # <class '__main__.calcClass'>

print(id(obj), id(obj2))
'''
2325243547952 2325243550784
'''
print('x =', obj2.x) # x = 100
print('y =', obj2.y) # y = 200


# Library class
# 1) built-in, import class

# 1. built-in class
a = int(10)
s = str('abc')
l = list([1,2,3,4])
a
s
l

# 2) import class
# import 'module' or,
# from 'module' import class1, class2 ...

from datetime import date

print(today.year, today.)