 c x# -*- coding: utf-8 -*-
"""
step03_continuous.py

 - 연속형 변수 시각화 : 산점도, 히스토그램, 박스 플롯
"""

import matplotlib.pyplot as plt # data 시각화
import numpy as np # data 생성

# 차트에서 한글 지원 : c:\windows\fonts
plt.rcParams['font.family'] = 'D2coding' #malgun.ttf

# 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False


# 1. 차트 자료 생성
data1 = np.arange(-3, 7) # -3 ~ 6
data2 = np.random.randn(10) # N(0, 1)
print(data1) # 이산형
print(data2) # 연속형

# 2. 산점도
plt.scatter(x=data1, y=data2, c='r', marker='o') # 단색
plt.title('산점도 시각화')
plt.show()

# 여러가지 색 산점도
cdata = np.random.randint(1,4, 10) # 1~3 정수 난수
print(cdata) # [1 2 1 3 2 1 2 3 1 2]

plt.scatter(x=data1, y=data2, c=cdata, marker='o') # 여러가지 색
plt.title('여러가지 색 산점도 시각화')
plt.show()


# 3. 히스토그램 : 대칭성 확인
# 표준정규분포
#data3 = np.random.randn(2000)  # (mean=0, sigma=1, size)
# 정규분포(mean=0, sigma=1)
data3 = np.random.normal(0, 1, 2000)  # (mean, sigma, size)
print(data3)

data4 = np.random.randn(2000)  # (mean, sigma, size)
print(data4)

# 난수 통계
data3.mean()  # -0.0038780272120932154
data3.std() # 1.0058492298262112

data4.mean() # -0.024711379379471467
data4.std() # 1.0274069136815878

# 정규분포 시각화
plt.hist(x=data3, bins = 100, density=True,
         histtype='step', label='data3')
plt.hist(x=data4, bins = 100, density=True,
         histtype='step', label='data4')
plt.legend(loc='best') # 범례
plt.show()
'''
bins : 계급 수
density : 빈도수(false) vs 밀도(true)
histtype : 'bar':세로막대형, 'step' : 다각분포형
'''

# 4. 상자 그래프(box plot) : 요약통계량 시각화
data5 = np.random.random(100) # 0~1 난수 실수
print(data5)

data5.mean() # 0.4728096258280577
data5.min() # 0.02352096973227169
data5.max() #  0.9871169167662582

plt.boxplot(x=data5)
plt.show()

type(data5) # numpy.ndarray

# numpy -> pandas
import pandas as pd

x = pd.Series(data5) # 1d

# 요약통계량 확인
x.describe()
type(x) # pandas.core.series.Series





















