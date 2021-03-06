# -*- coding: utf-8 -*-
"""
step04_category

@author: wonseok
"""

import matplotlib.pyplot as plt # data 시각화
import numpy as np # data 생성

# 차트에서 한글 지원 : c:\windows\fonts
plt.rcParams['font.family'] = 'D2coding' #malgun.ttf

# 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# 차트 자료 생성
data = [127, 90, 201, 150, 250] # 국가별 수출현황
idx = np.arange(1, len(data) + 1)
labels = list(['싱가폴', '태국', '한국', '일본', '미국'])

# 2. 세로 막대
plt.bar(idx, data)
plt.title('국가별 수출 현황')
plt.xlabel('국가별')
plt.ylabel('수출 현황 (단위: 십억 달러)')
plt.show()

# 3. 가로 막대
plt.barh(y = idx, width = data)
plt.title('국가별 수출 현황')
plt.xlabel('수출 현황 (단위: 십억 달러)')
plt.ylabel('국가별')
plt.show()


# 4. pie chart
plt.pie(data, labels = labels)
