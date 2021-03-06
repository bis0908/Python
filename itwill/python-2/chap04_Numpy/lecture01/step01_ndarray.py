# -*- coding: utf-8 -*-
"""
step01_ndarray

Numpy Package 특징
    - 수치 과학용 데이터 처리 목적으로 사용
    - 선형대수(벡터, 행렬) 연산 관련 함수 제공
    - list 보다 이점
        -> N차원 배열, 선형대수, 고속 연산
        -> 수학/ 통계 관련 함수
        -> indexing
        -> broadcast 연산: 1d vs scala
@author: wonseok
"""

import numpy as np

# 1. list 배열 vs 다차원 배열

# 1.1
lst = [1, 2, 3, 3.5]    # 정수, 실수: 다양한 자료형

lst * 0.5   # 1d * 0d (scala)
lst * 3     # 3회 반복
sum(lst)    # 외부 함수의 도움을 받아야 함. lst.sum() 이런거 안됨

# 1.2 다차원 배열
arr = np.array(lst)     # list -> 다차원 배열

# broadcast 연산: 서로 다른 차원 간 연산 가능
arr * 0.5   # [0.5 , 1.  , 1.5 , 1.75]
arr.sum()
arr.mean()

arr[-1]     # indexing
# 자료 모양
arr.shape   # (4, ) -> 1d



# 2. array(): 다차원 배열 생성
# array([[[var1, var2, ...]]])

# 2.1 단일 list: [] -> 1차원 배열
lst1 = [3, 5.3, 4, 7]

# list -> array
arr1d = np.array(lst1) # array([3, 5.3, 4, 7])

arr1d.shape     # (4,) -> 1d

# 수학/통계 함수
arr1d.mean()    # 4.825
arr1d.var()     # 산포도(): 2.241875
arr1d.std()     # 표준편차(): 1.4972892172189045


# 2.2 중첩 list: [[]] -> 2차원 배열
lst2 = [[1,2,3,4], [5,6,7,8]]

arr2d = np.array(lst2)
arr2d
# [[1, 2, 3, 4],
#  [5, 6, 7, 8]]

arr2d.shape # (2,4) -> 2d (행, 열)

# 3. broadcast 연산
# low -> high dimension

# 1. scala(0d) vs vector(1d)
0.5 * arr1d # [1.5 , 2.65, 2.  , 3.5 ]

# 2. scala(0d) vs matrix(2d)
0.5 * arr2d

# 3. vector(1d) vs matrix(2d)
arr1d * arr2d

# 4. zeros(), ones()
zarr = np.zeros((3, 10))    # (행, 열): 0으로 채워진 행렬. 희소행렬 만들때 쓰임
zarr    #  희소행렬: 문장 vs 단어
#       a,  b   c   d   ...
# doc1 [1., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
# doc2 [0., 2., 0., 0., 0., 0., 0., 0., 0., 0.],
# doc3 [2., 1., 0., 0., 0., 0., 0., 0., 0., 0.]

np.ones((3, 10))
# [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
# [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
# [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]


# 5. arrange(): range(n), range(n, m) range(n, m, s)

# 5.1 range vs arange
list(range(1, 11))
np.arange(1, 11)

# 차이점: float 사용 여부
range(-0.1, 10.5) # Err!
np.arange(-0.1, 10.5) # [-0.1,  0.9,  1.9,  2.9,  3.9,  4.9,  5.9,  6.9,  7.9,  8.9,  9.9]

# ex. x의 수열에 대한 2차 방정식
x = np.arange(-1.0, 2, 0.1)
len(x)

y = x**2 + 2*x + 3
y

# 2차 방정식 그래프
import matplotlib.pyplot as plt
plt.plot(x, y)

# 색인 반환
zarr.shape

# 카운터 값 채우기
cnt = 0
for i in np.arange(3):  # 행 index [0, 1, 2]
    for j in np.arange(10):  # 열 index [0 ~ 9]
        cnt += 1
        zarr[i, j] = cnt

zarr



