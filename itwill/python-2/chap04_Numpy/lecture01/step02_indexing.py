# -*- coding: utf-8 -*-
"""
step02_indexing

다차원 배열의 원소 참조 방식
    - 1차원 배열: list 동일
    - 2, 3차원 배열 indexing
    - 조건식 색인

@author: wonseok
"""

import numpy as np

# indexing

# 1차원: obj[index]
# 2차원: obj[행 index, 열 index]
# 3차원: obj[면 index, 행 index, 열 index]


arr = np.arange(10) # 0 ~ n-1
arr

arr[:] # 전체 원소
arr[3]

# 2. slicing

# 주소 복제
arr_obj = arr[1:4]
arr_obj[:] = 100    # [100, 100, 100] -> 전체 수정

# 원본도 수정이 되버림 (주소가 복제 되었기 때문에)
arr     # [  0, 100, 100, 100,   4,   5,   6,   7,   8,   9]

# 내용 복제 (하지만 원본 데이터는 그대로 유지됨)
arr_obj2 = arr[1:4].copy()
arr_obj2[:] = 200
arr # [  0, 100, 100, 100,   4,   5,   6,   7,   8,   9] <- 그대로 유지된다 !



# 3.고차원 색인 (index)

# 2d indexing
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d
# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]])

arr2d.shape # (3, 3)

# 2차원: 행 index 기본
arr2d[0, :] # == arr2d[0]



arr2d[:2, :2]
arr2d[::2]  # 홀수행 선택 [start:step:step]

arr2d[::2, ::2] # 홀수 행렬
# [[1, 3],
#  [7, 9]]

arr2d[[0,2]] # 비연속 행렬
# [[1, 2, 3],
#  [7, 8, 9]]

# 3.2 3차원 색인
arr3d = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
arr3d.shape

# 면 선택
arr3d[1]
arr3d[1,1]
arr3d[1,1,:2]

# 4. 조건식 색인
dataset = np.random.randn(3,4)
dataset

# 0.2 이상 선택
dataset[dataset >= 0.2] # 하나 이상의 조건 들어갈 시 에러 발생함

# 논리식 - Numpy
np.logical_and()
np.logical_or()
np.logical_not()
np.logical_xor()

dataset[np.logical_and(dataset >= 0.1, dataset <= 0.7)] # 이렇게 써야 함
dataset[np.logical_or(dataset >= 0.1, dataset <= 0.7)]


# pandas case
import pandas as pd
ser = pd.Series([1,2,3,4,5])
ser[ser >= 2]

# ser[ser>=2 and ser <= 4] # Err!
ser[np.logical_and(ser >= 2, ser <= 4)] # pd 에서도 np 사용



