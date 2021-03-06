# -*- coding: utf-8 -*-
"""
선형대수(inear algebra) 관련 함수 : ppt.57 참고
- 선형적(linear)인 모양의 자료를 대상으로 수의  관계를 연구하는 대수학의 한 분야
"""

import numpy as np

# 1. 선형대수 관련 함수

# 1) 단위행렬 : 대각원소가 1이고, 나머지는 모두 0인 n차 정방행렬
eye_mat = np.eye(3)
print(eye_mat)


# 2) 대각행렬 : 대각성분 이외의 모든 성분이 모두 '0'인 n차 정방행렬
x = np.arange(1,10).reshape(3,3)
print(x)

diag_vec = np.diag(x)
print(diag_vec)

# 대각행렬 = 단위행렬 * 대각성분
diag_mat = eye_mat * diag_vec
print(diag_mat)


# 3) 대각합 : 정방행렬의 대각에 위치한 원소들의 합
trace_scala = np.trace(diag_mat) # 2차원
print(trace_scala) # [1 5 9] = 15.0


# 4) 행렬식 : 대각원소의 곱과 차 연산으로 scala 반환
x = np.array([[3,4], [1,2]])
print(x)


det_scala = np.linalg.det(x)
print(det_scala)


# 5) 역행렬 : 행렬식의 역수를 정방행렬 대응 곱셈
inv_mat = np.linalg.inv(x)
print(inv_mat)

# 1.6 행렬 곱: A @ B
a = np.array([[1,1],[0,1]])
b = np.array([[2,3],[1,5]])

matmul = a.dot(b)
matmul

matmul2 = a@b
matmul2
'''
행렬곱 연산시 주의사항
1. 모두 행렬일것.
2. 수 일치: A(열수) = B(행수)
'''

