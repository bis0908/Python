# -*- coding: utf-8 -*-
"""
step05_correlation

상관분석: 두 변수간의 상관성 분석

공분산 vs 상관계수

1. 공분산: 두 변수간의 분산(평균에서 퍼짐 정도)을 나타내는 통계
    - Cov(X, Y) = sum((X - xmu) * (Y - ymu)) / n
    - Cov(X, Y) > 0: 두 변수 비례
    - Cov(X, Y) < 0: 두 변수 반비례
    - Cov(X, Y) = 0: 상관성 없음
    - X의 편차와 Y의 편차를 곱한것의 평균!

2. 상관계수: 공분산을 각각 표준편차로 나누어 정규화(-1 ~ +1) 통계
    - 부호는 공분산과 동일, 절대값 1을 넘지 않음
    - Corr(X, Y) = Cov(X, Y) / std(X) * std(Y)
@author: wonseok
"""

import pandas as pd
import os
os.chdir('E:\Code\Python\itwill\python-2\data')

iq = pd.read_csv('score_iq.csv')

iq.info()

# 상관계수
iq.head()

corr = iq.corr(method = 'pearson')
corr

# 변수 vs 변수
iq['score'].corr(iq['iq'])  # 0.8822203446134705
iq['score'].corr(iq['academy'])     # 0.8962646792534942

# 2. 공분산
cov = iq.cov()

# 공분산 행렬
cov

# 변수 vs 변수
iq['score'].cov(iq['iq']) # 51.337539149888144
iq['score'].cov(iq['academy']) # 7.119910514541386

# 식 적용
# Cov(X, Y) = sum((X - xmu) * (Y - ymu)) / n
X = iq['score']
Y = iq['iq']
xmu = X.mean()
ymu = Y.mean()

Cov = sum((X - xmu) * (Y - ymu)) / (len(X) - 1)
Cov  # 51.33753914988811

Corr = Cov / (X.std() * Y.std())
Corr # 0.8822203446134699
