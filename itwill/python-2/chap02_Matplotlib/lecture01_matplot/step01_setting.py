# -*- coding: utf-8 -*-
"""
step01_setting.py

- 한글 사용, 음수 부호 적용
"""

import matplotlib.pyplot as plt # data 시각화 
import numpy as np # data 생성 

# 차트에서 한글 지원 : c:\windows\fonts
plt.rcParams['font.family'] = 'HYGothic-Extra'#'Malgun Gothic'#malgun.ttf

# 폰트 이름 찾기 : malgun.ttf -> Malgun Gothic
path = 'C:\\Windows\Fonts\\H2GTRE.TTF' #'malgun.ttf'
import matplotlib.font_manager as fm 

font_name = fm.FontProperties(fname=path).get_name()
print(font_name) # Malgun Gothic, HYGothic-Extra



# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False


# 1. data 생성 
data = np.random.randn(100) # 정규분포 난수 100개 생성 
print(data)

# 2. 정규분포 시각화
plt.plot(data) # 시각화 
plt.title('정규분포 시각화') # 제목 
plt.xlabel('색인') # x축 이름 
plt.ylabel('난수') # y축 이름 
plt.show() # 화면 보이기 












