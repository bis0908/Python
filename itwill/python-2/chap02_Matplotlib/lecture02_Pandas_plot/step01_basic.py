# -*- coding: utf-8 -*-
"""
step01_basic

Pandas 객체 시각화
형식) obj.plot(kind = '차트 유형', 속성)
        plt.show()

    kind = bar, pie, hist, kde, scatter(산점도), box
@author: wonseok
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 기본 차트 시각화
ser = pd.Series(np.random.randn(10))
ser

# 1차원 객체: 기본차트 - 선 그래프
ser.plot(color = 'g')
ser.plot()

# 2차원 객체
df = pd.DataFrame(np.random.rand(10,4), columns = ('one', 'two', 'three', 'four'))
df
df.plot() # 기본 차트

# 막대차트: 세로
df.plot(kind = 'bar', title = 'bar chart')

# 막대차트: 가로
df.plot(kind = 'barh', title = 'barh chart')

# 막대차트: 가로 + 누적형
df.plot(kind = 'barh', title = 'barh chart', stacked = True)

# dataset 이용
import os
os.chdir('E:\Code\Python\itwill\python-2\data')
tips = pd.read_csv('tips.csv')
tips.info()

# 교차분할표: 집단변수 이용
# 요일(day) vs 규모(size)
tips['day'].unique()    # ['Sun', 'Sat', 'Thur', 'Fri']
tips['size'].unique()   # [2, 3, 4, 1, 6, 5]

tab = pd.crosstab(tips['day'], columns = tips['size'])
tab.shape   # 4, 6

tab.index   # ['Fri', 'Sat', 'Sun', 'Thur']
tab.columns     # [1, 2, 3, 4, 5, 6]

# tab.index = [] -> 행 이름 변경
type(tab)   # pandas.core.frame.DataFrame

# size: 1, 6 제외 -> subset
# obj.loc[행, 열]
new_tab = tab.loc[:, 2:5]
new_tab

# 교차분석 시각화
tab.plot(kind = 'barh', stacked = True, title = 'day n size')

help(tab.plot)  # 도움말


