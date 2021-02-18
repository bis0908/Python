# -*- coding: utf-8 -*-
"""
step06_func_deco

함수 장식자
- 특정 함수를 꾸미는 역할의 함수

@함수장식자

@author: wonseok
"""

# 함수 장식자 정의
def hello_deco(func):
    def inner(name):
        print('*' * 30)
        func(name)
        print('*' * 30)
    return inner

# 함수 장식자 적용
@hello_deco
def hello(name):
    print('my name is '+ name)

hello('kong wonseok')

