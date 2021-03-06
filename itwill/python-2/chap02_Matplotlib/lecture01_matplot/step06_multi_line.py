# -*- coding: utf-8 -*-
"""
step06_multi_line

marker, color, label, linestyle

@author: wonseok
"""

import matplotlib.pyplot as plt # data 시각화
import numpy as np # data 생성

# 차트에서 한글 지원 : c:\windows\fonts
plt.rcParams['font.family'] = 'D2coding' #malgun.ttf

# 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# 1. data 생성: 평균 + 표준편차 * 난수
data1 = 0.5 + 0.3 * np.random.randn(100)
data2 = 0.7 + 0.2 * np.random.randn(100)
data3 = 0.9 + 0.1 * np.random.randn(100)
data4 = 0.3 + 0.4 * np.random.randn(100)

# 2. figure 객체
fig = plt.figure(figsize = (12, 5))
chart = fig.add_subplot()

# 3. plot 시각화
chart.plot(data1, marker = 'o', color = 'blue', linestyle = '-', label = 'data1')
chart.plot(data2, marker = '*', color = 'red', linestyle = '--', label = 'data2')
chart.plot(data3, marker = 's', color = 'green', linestyle = '-.', label = 'data3')
chart.plot(data4, marker = '+', color = 'orange', linestyle = ':', label = 'data4')

chart.set_title('multi lines: marker, color, linestyle, labels')
plt.legend(loc = 'best')
plt.show()


