# -*- coding: utf-8 -*-
"""
step04_reshape

1. 행렬 모양 변경하기
    obj.reshape()
        - 1차원 -> 2차원
        - 2차원 -> 다른 2차원 변경
        - 2차원 -> 3차원

2. 전치행렬: T
@author: wonseok
"""

import numpy as np

# 1. reshape
arr1d = np.arange(1, 13)
arr1d.shape

arr2d = arr1d.reshape(3, 4)
arr2d.shape # (3, 4)

# 주의: 원소 size 수정 불가
arr1d.reshape(2, 6) # 12
# arr1d.reshape(2, 5) # error

arr3d = arr2d.reshape(2, 3, 2)
arr3d

# 2. 전치 행렬
arr2d_T = arr2d.T
arr2d_T.shape # (4, 3)

# 3. swap axes: 행렬 축 교환
arr2d.swapaxes(0, 1)

# 4. transpose
# 1차원: 효과 없음
# 2차원: 전치행렬
# 3차원: 축 순서를 이용

arrd3 = np.arange(1, 25).reshape(4, 2, 3)
arr3d.shape

arr3d_def = arr3d.transpose() # default: (0, 1, 2) -> (2, 1, 0)
arr3d_def.shape

# (0, 1, 2) -> (2, 1, 0)
arr3d_user = arr3d.transpose(2, 0, 1)
arr3d_user.shape
