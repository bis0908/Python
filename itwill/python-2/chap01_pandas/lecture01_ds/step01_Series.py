# -*- coding: utf-8 -*-
"""
step01_Series.py

Series 객체 특징 
 - pandas 1차원 자료구조(vector)
 - DataFrame의 칼럼 사용 
 - 수학/통계 함수 제공 
 - 범위 수정, 블럭 연산 
 - indexing/slicing 기능 
"""

import pandas as pd # pd.Series()
from pandas import Series # Series()


# 1. Series 객체 생성 : list 
# 1) list 이용 
price = pd.Series([4000, 3000, 3500, 2000])
print(price)

# object.member : 속성 or object.mebmer() : 메서드 
price.index # 색인 
price.values # 값 
'''
 RangeIndex(start=0, stop=4, step=1)
 array([4000, 3000, 3500, 2000], dtype=int64)
'''

price[1] # 값 참조 : 3000
price.drop(0) # 원소 제거 

# index 적용 
price2 = pd.Series(data = [4000, 3000, 3500, 2000],
                   index = ['a','b','c','d'])
print(price2)

price2['c'] # 3500

# 조건식 
price2[price2 >= 3500]
'''
a    4000
c    3500
'''

# 2) dict : {'key' : value} -> key : index, value : values
person = Series({'name':'홍길동', 'age':35, 'addr' : '서울시'})
print(person)

person['name'] # '홍길동'


# 2. indexing : list 동일 
ser = pd.Series([4, 5, 6.5, 7, 9]) # 정수, 실수형 
print(ser) # dtype: float64

ser[0]
ser[:3]
ser[3:]
ser[:] # 전체 
# ser[-1] # 주의 : 오류 

# 3. Series 결합과 NA 처리 
s1 = pd.Series([4000, 3000, 3500, 2000],
               index = ['a','b','c','d'])

s2 = pd.Series([4000, None, 3500, 2000],
               index = ['a','c','b','e'])

# Series 결합 : index 기준 
s3 = s1 + s2
print(s3)
'''
a    8000.0
b    6500.0
c       NaN -> 결측치 
d       NaN
e       NaN
'''

# 결측치 처리 : 대표값(평균)
s4 = s3.fillna(s3.mean())
print(s4)
'''
a    8000.0
b    6500.0
c    7250.0
d    7250.0
e    7250.0
'''

# 결측치 처리 : 특정 상수(0)
s5 = s3.fillna(0)
print(s5)

# 결측치 제거 
s6 = s3[pd.notnull(s3)]
print(s6)


# 4. Series 연산 
print(ser, len(ser)) # dtype: float64 5

# 1) 블럭 수정 
ser[1:4] = 30
print(ser)

# 2) broadcast 연산 : 1d(vector) vs 0d(scala)
ser.shape # (5,) -> 1차원(5개 원소)
print(ser * 0.5)  # 1d * 상수(0d)

# list vs series 
lst = [1,2,3,4,5] # list
lst * 0.5 # TypeError
for i in lst :
    print(i*0.5)
    
# lsit -> Series 
ser = pd.Series(lst)    
ser * 0.5 # 벡터 연산 


# 3) 수학/통계 함수 
ser.mean() 
ser.sum()
ser.max()
ser.min()

# object의 멤버 확인 
dir(ser)

ser.std()
ser.var()
re = ser.add(-10) # -10 덧셈 
print(ser) # 현재 객체 수정 안됨  
print(re) # 새로운 객체 수정 

