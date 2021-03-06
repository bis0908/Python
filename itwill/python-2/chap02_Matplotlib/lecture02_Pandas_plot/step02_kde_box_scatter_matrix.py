# -*- coding: utf-8 -*-
"""
step02_kde_box_scatter_matrix

pandas 객체 대상 연속형 변수 시각화
    - hist, kde, box, scatter matrix

@author: wonseok
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. KDE (Kernel density estimation): 커널 밀도 추정

# 1.1 Data 생성
df = pd.DataFrame(np.random.rand(10, 4), columns = ['a', 'b', 'c', 'd'])
df

# 1.2 hist
df['a'].plot(kind = 'hist', title = 'histogram')

# 1.3 kde: 확률 밀도 분포 곡선
df['a'].plot(kind = 'kde', title = 'kde')

# 전체 확률 변수 대상
df.plot(kind = 'kde', title = 'Kernel density plot')

# 2. box plot
df.plot(kind = 'box', title = 'box plot')

df.describe()

# 3. scatter matrix
from pandas.plotting import scatter_matrix as sm

sm(df)

import os
os.chdir('E:\Code\Python\itwill\python-2\data')

iris = pd.read_csv('iris.csv')

cols = list(iris.columns)
cols
x = iris[cols[:4]]
x.shape

sm(x, diagonal = 'kde')
