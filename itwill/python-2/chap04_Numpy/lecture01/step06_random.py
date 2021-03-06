# -*- coding: utf-8 -*-
"""
step06_random

- 난수 제공 관련 함수
- 표본 추출
- 표본의 확률분포 실험

@author: wonseok
"""

import numpy as np

# 1. 난수 실수와 정수

# 1.1 난수 실수: [0, 1]
data = np.random.rand(5, 3) # (행, 열)
data

# 난수 통계
data.max()
data.min()
data.mean()

# 1.2 난수 정수: [최소값, 최대값)
data2 = np.random.randint(165, 175, 50) # key sample
data2.shape

# 난수 통계
data2.max()
data2.min()
data2.mean()

# 2. 정규분포와 표준정규분포

# 2.1 정규분포: N(평균, 표준편차^2)
height = np.random.normal(173, 5, 2000)
height

height2 = np.random.normal(173, 5, (500, 4))

# 난수 통계
height.mean()
height.std()

height2.mean()
height.std()

import matplotlib.pyplot as plt
plt.hist(height, bins = 100, density = True, histtype = 'step')


# 2. 표준정규분포: N(0, 1)
stNorm = np.random.randn(500, 3)
stNorm.shape

# 난수 통계
stNorm.mean()
stNorm.std()

plt.hist(stNorm[:, 0], bins = 100, density = True, histtype = 'step', label = 'col1')
plt.hist(stNorm[:, 1], bins = 100, density = True, histtype = 'step', label = 'col2')
plt.hist(stNorm[:, 2], bins = 100, density = True, histtype = 'step', label = 'col3')
plt.legend(loc = 'best')

'''
표준 정규 분포의 확률 분포
-1 ~ +1: 68%
-2 ~ +2: 95%
-3 ~ +3: 99%
'''

# z 공식: 정규분포 -> 표준정규분포
# z = (x - mu) / sigma

mu = height.mean()
sigma = height.std()

z = (height - mu) / sigma
z.mean()
z.std()

plt.hist(z, bins = 100, density = True, histtype = 'step')


# 3. dataset sample

# 3.1 dataset load
import pandas as pd
path = 'E:/Code/Python/itwill/python-2/data/'
wdbc = pd.read_csv(path + 'wdbc_data.csv')

wdbc.info()
# RangeIndex: 569 entries, 0 to 568
# Data columns (total 32 columns)

# seed value
np.random.seed(123)

wdbc_df = wdbc.sample(400)
wdbc_df.shape

wdbc_df.head()


# numpy.random 함수 이용
idx = np.random.choice(a =len(wdbc), size = 400, replace = False)
idx

wdbc_sample = wdbc.iloc[idx] # 위치 기반 색인
wdbc_sample.shape

wdbc_sample.head()

# list + for
test_idx = [i for i in range(len(wdbc)) if not i in idx]
wdbc_test = wdbc.iloc[test_idx]

wdbc_test.shape
