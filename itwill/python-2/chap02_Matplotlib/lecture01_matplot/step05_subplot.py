# -*- coding: utf-8 -*-
"""
step05_subplot
- plot 공간을 행렬로 나누어 시각화


@author: wonseok
"""

import matplotlib.pyplot as plt # data 시각화
import numpy as np # data 생성

# 차트에서 한글 지원 : c:\windows\fonts
plt.rcParams['font.family'] = 'D2coding' #malgun.ttf

# 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# 1. figure 객체 & subplot
fig = plt.figure(figsize = (10, 5)) # 차트 크기 설정

x1 = fig.add_subplot(2, 2, 1)   # 2행 2열 1번
x2 = fig.add_subplot(2, 2, 2)
x3 = fig.add_subplot(2, 2, 3)
x4 = fig.add_subplot(2, 2, 4)   # ~ 4번

# 2. 차트 자료 생성
data1 = np.random.randn(100) # 난수 실수
data2 = np.random.randint(1, 100, 100) # 난수 정수
data3 = np.random.randint(1, 4, 100) # 난수 정수
data1
data2
data3

# 3. subplot 차트 그리기
x1.hist(data1)
x2.scatter(data1, data2, c = data3)
x3.plot(data2)
x4.plot(data2, 'g--')
plt.show()