# -*- coding: utf-8 -*-
"""
step02_basic_plot.py

 - 기본 차트 시각화
"""

import matplotlib.pyplot as plt # data 시각화
import numpy as np # data 생성

# 차트에서 한글 지원 : c:\windows\fonts
plt.rcParams['font.family'] = 'D2coding' #malgun.ttf

# 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# 1. 차트 자료 만들기
data = np.arange(-3, 7) #arange(start, stop)
print(data)
len(data) # 10


# plot함수 정보
help(plt.plot)
'''
plot(x, y)        # plot x and y using default line style and color
plot(x, y, 'bo')  # plot x and y using blue circle markers
plot(y)           # plot y using x as index array 0..N-1
plot(y, 'r+')     # ditto, but with red plusses
'''

# 2. 기본 선 스타일과 색상
plt.plot(data) # 그리기 : plot(index, data)
plt.title("기본 선 스타일과 색상 지원")
plt.show() # 보이기

# 3. 스타일 점선, 색상 빨강
plt.plot(data, 'r--')
plt.title("선 스타일 --, 선색은 빨강")
plt.show() # 보이기

# 4. x,y축 선 스타일과 색상
data2 = np.random.randn(10)

plt.plot(data, data2)
plt.title("x, y축 기본 선 스타일과 색상")
plt.show() # 보이기

# marker = 'o' or marker = '.'
plt.plot(data, data2, 'bo') # 'bo', 'ro', 'r.'
plt.title("color, marker")
plt.show() # 보이기







