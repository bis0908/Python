# -*- coding: utf-8 -*-
"""
step04_model_plot

- 분석모델 관련 시각화

@author: wonseok
"""

import matplotlib.pyplot as plt
import seaborn as sb

# 차트에서 한글 지원 : c:\windows\fonts
plt.rcParams['font.family'] = 'D2coding' #malgun.ttf

# 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# dataset load
sb.get_dataset_name() # Data lists

flights = sb.load_dataset('flights')
iris = sb.load_dataset('iris')

# 1. 오차대역폭을 갖는 시계열: x, y (시간축, 통계량)
flights.info()
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   year        144 non-null    int64
#  1   month       144 non-null    category
#  2   passengers  144 non-null    int64

sb.lineplot(x = 'year', y = 'passengers', hue = 'month', data = flights)

# 2. 회귀분석: 산점도 + 회귀선
iris.info()

x = iris.sepal_length
y = iris.petal_length


# ci: 신뢰구간의 신뢰수준
sb.lmplot(x = 'sepal_length', y = 'petal_length', ci = 95, data = iris)

# hue 추가: 꽃종 별 회귀선
sb.lmplot(x = 'sepal_length', y = 'petal_length', ci = 95, hue = 'species',  data = iris)


# 3. heatmap: 분류결과 시각화
import pandas as pd
y_true = pd.Series([1, 0, 1, 0, 1])
y_pred = pd.Series([1, 0, 1, 0, 0])

# 교차분할표
tab = pd.crosstab(index = y_true, columns = y_pred)
tab

acc = (tab.iloc[0,0] + tab.iloc[1,1]) / len(y_true)
acc

# heatmap
sb.heatmap(data = tab, annot = True)
plt.xlabel('real value')
plt.ylabel('predicted values')
plt.title('분류 정확도 = {}'.format(acc), size = 18)

