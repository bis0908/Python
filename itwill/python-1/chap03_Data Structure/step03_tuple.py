# -*- coding: utf-8 -*-
"""
tulpe
특징
- 1차원 배열 구조
- index 사용(순서 존재)
- 형식) 변수 = (x1, x2, ..., n)
- 수정 불가, list보다 속도 빠름

@author: wonseok
"""

# tuple 생성
tp = (10)
print(tp, type(tp)) # 10 <class 'int'>

tp = (10,)
print(tp, type(tp)) # (10,) <class 'tuple'>

tp1 = (1, 2, 3, 4, 5)
print(tp1, type(tp1), len(tp1))

tp1[3]

# indexing
tp1[:]
tp1[0]
tp1[-1]

# 객체의 원소는 삭제 불가하다
tp[2] = 'three' # TypeError: 'tuple' object does not support item assignment

dataset = (10, 5, 2.3, 80, 54)

dir(dataset) # count, index

dataset.count(54) # 갯수
dataset.index(54) # 위치는?

# tuple + zip() - vector 원소 묶기
names = ['kim', 'kong', 'ko']
pays = [200, 300, 400]

emps = list(zip(names, pays))
print(emps)
len(emps)

type(emps)
type(emps[0])
