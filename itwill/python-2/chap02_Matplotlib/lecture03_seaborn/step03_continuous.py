# -*- coding: utf-8 -*-
"""
step03_continuous

연속형 변수 시각화: 히스토그램, kde, scatter matrix, box

@author: wonseok
"""

import matplotlib.pyplot as plt
import seaborn as sb

# dataset load
iris = sb.load_dataset('iris')
iris.info()

tips = sb.load_dataset('tips')
tips.info()

# 1. hist
x = iris.sepal_length
x.hist()

# 2. distplot(): hist, kde -> matplotlib의 hist 그래프와 kdeplot을 통합한 그래프 이며, 분포와 밀도를 확인할 수 있다.
sb.distplot(x, hist = True)

# 3. scatter matrix
sb.pairplot(iris, hue = 'species') # hue: color

# 4. scatter(산점도): x: 연속형, y: 연속형
sb.scatterplot(x = 'sepal_length', y = 'petal_length', hue = 'species', data = iris)

# 5. 변수의 통계적 관계: 연속형 vs 연속형 [집단변수]
sb.relplot(x = 'total_bill', y = 'tip', hue = 'sex', data = tips)

# 6. box plot: 범주형 vs 연속형
sb.boxplot('day', y = 'total_bill', data = tips) # 요일별 vs 총 지불 금액

# 범주형 vs 연속형 [집단변수]: 성별에 따른 요일별 행사 총 지불 금액
sb.boxplot('day', y = 'total_bill', hue = 'sex', data = tips)




