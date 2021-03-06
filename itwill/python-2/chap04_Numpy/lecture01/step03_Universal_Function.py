# -*- coding: utf-8 -*-
"""
step03_Universal_function.py

유니버셜 함수 
 - 다차원 배열의 원소를 대상으로 한 수학/통계 관련 함수 
"""

import numpy as np 

# 1. numpy 제공 함수 
data = np.random.randn(10) # 1d
data

np.abs(data) # 절댓값 
np.sqrt(data) # 제곱근 
np.square(data) # 제곱(data ** 2) 
np.sign(data) # 부호 판단 
np.var(data) # 분산
np.std(data) # 표준편차 


data2 = np.array([1, 2.5, 3.36, 4.6])
np.log(data2) # 밑수 e : data 정규화 
# [0.        , 0.91629073, 1.21194097, 1.5260563 ]

np.exp(data2)
# [ 2.71828183, 12.18249396, 28.78919088, 99.48431564]

# 반올림 함수 
np.ceil(data2) # [1., 3., 4., 5.] : # 큰 정수 
np.floor(data2) # [1., 2., 3., 4.] : 작은 정수 
np.rint(data2) # [1., 2., 3., 5.] : 가장 가까운 정수 
np.round(data2, 1) # 자릿수 반올림 : [1. , 2.5, 3.4, 4.6]

# 결측치 처리 
data2 = np.array([1, 2.5, 3.36, 4.6, np.nan])
print(data2) # [1.   2.5  3.36 4.6   nan]

np.isnan(data2)
# [False, False, False, False,  True]

# 결측치 제외 -> subset 

data2[np.logical_not(np.isnan(data2))] 
# [1.  , 2.5 , 3.36, 4.6 ]

data2[~np.isnan(data2)] # ~ : not 
# [1.  , 2.5 , 3.36, 4.6 ]


# 2. 객체.메서드()
data3 = np.random.randn(3, 4)

data3.shape

# 전체 자료 통계 
data3.sum() # 전체 합계 - scala
data3.var()
data3.std()
data3.mean()
data3.max()
data3.min()

# 3. axis 속성 
'''
axis = 0 : 행축 - 열 단위 
axis = 1 : 열축 - 행 단위
'''
data3.sum(axis = 0) # 열 단위 합계 
# [ 0.25061606, -0.72270039,  3.20982414,  2.59312984]
data3.sum(axis = 1) # 행 단위 합계 
# [ 3.66342806,  2.87310865, -1.20566706] 







