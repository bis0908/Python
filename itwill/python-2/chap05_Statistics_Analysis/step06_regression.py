# -*- coding: utf-8 -*-
"""
step06_regression

scipy 패키지 제공
    1. 단순 선형 회귀 분석
    2. 다중 선형 회귀 분석

@author: wonseok
"""

from scipy import stats # test
import os
import pandas as pd # csv file read

os.chdir('E:\Code\Python\itwill\python-2\data')

iq = pd.read_csv('score_iq.csv')

iq.info()

# 1. 단순 선형 회귀 분석
# formula: x -> y

# 1.1 변수 선택
x = iq['iq'] # 독립변수 만들기
y = iq['score']

# 1.2 model 생성
model = stats.linregress(x, y)
model

# =============================================================================
# LinregressResult(slope=0.6514309527270081, -> x 기울기
#                  intercept=-2.856447122197551, -> y 절편
#                  rvalue=0.8822203446134705, -> 설명력
#                  pvalue=2.8476895206672287e-50, -> F검정 - 모델 유의성 검정
#                  stderr=0.028577934409305377) -> 표준 오차
# =============================================================================

a = model.slope
b = model.intercept

# 회귀 방정식: y = (X * a) + b
iq.head(1)

iq = 140
score = 90

# 적합값
fitted_value = (iq * a) + b
fitted_value # 88.34388625958358

# 오차
err = score - fitted_value
err # 1.6561137404164157

# 전체 관측치 대상
fitted_value = (x * a) + b

# 관측값 vs 예측값
fitted_value.mean() # 77.77333333333334
y.mean() # 77.77333333333334

fitted_value[:10]
y[:10]

# 1.3 산점도와 회귀선 시각화
from pylab import plot, title, legend, show

# 산점도
plot(x, y, 'ob')
plot(x, fitted_value, 'r-')
title('linear regression')
legend(['x, y scatter', 'linear regression'])



# 2. 다중 선형 회귀 분석
# =============================================================================
# formula: y ~ x1 + x2 + x3 + ...
# =============================================================================
from statsmodels.formula.api import ols

wine = pd. read_csv('winequality-both.csv')
wine.info()

wine.columns = wine.columns.str.replace(' ', '_')
wine.info()

# 상관계수 행렬
corr = wine.corr()
corr

corr['quality']
# x1 = alcohol, x2 = chlorides, x3 = citric_acid
# y = quality

formula = 'quality ~ alcohol + chlorides + citric_acid'
obj = ols(formula = formula, data = wine) # class -> object

obj

model = obj.fit() # model

# 회귀분석 결과 제공
model.summary()

#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                quality   R-squared:                       0.214
# Model:                            OLS   Adj. R-squared:                  0.214
# Method:                 Least Squares   F-statistic:                     590.0
# Date:                Wed, 03 Mar 2021   Prob (F-statistic):               0.00
# Time:                        13:51:25   Log-Likelihood:                -7554.8
# No. Observations:                6497   AIC:                         1.512e+04
# Df Residuals:                    6493   BIC:                         1.514e+04
# Df Model:                           3
# Covariance Type:            nonrobust
# ===============================================================================
#                   coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------
# Intercept       2.5428      0.096     26.616      0.000       2.355       2.730
# alcohol         0.3079      0.008     36.947      0.000       0.292       0.324
# chlorides      -2.3996      0.284     -8.451      0.000      -2.956      -1.843
# citric_acid     0.5631      0.066      8.511      0.000       0.433       0.693
# ==============================================================================
# Omnibus:                      121.605   Durbin-Watson:                   1.657
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              253.539
# Skew:                           0.014   Prob(JB):                     8.80e-56
# Kurtosis:                       3.967   Cond. No.                         317.
# ==============================================================================

# 회귀 계수 값 (coef)
b = 2.5428
a1 = 0.3079
a2 = -2.3996
a3 = 0.5631

# =============================================================================
# 다중 회귀 방정식
# fittedValue = (X1 * a1 + X2 * a2 + X3 * a3) + b
# fittedValue = dot(X, a) + b -> 행렬 곱
# =============================================================================

fittedvalue = model.fittedvalues
fittedvalue

# 적합값 vs 관측값
fittedvalue.mean() # 5.8183777127904355
quality = wine['quality']
quality.mean() # 5.818377712790519

import numpy as np

X = wine[['alcohol', 'chlorides', 'citric_acid']]
X.shape # (6497, 3)

a = np.array([[a1], [a2], [a3]])
a.shape # (3, 1)

fittedValue = np.dot(X, a) + b

fittedValue.mean() # 5.818188984730371

# 차트 보기
import matplotlib.pyplot as plt

plt.plot(fittedValue[:100], label = 'y predicted')
plt.plot(quality[:100], label = 'y real values')
plt.legend(loc = 'best')
plt.yticks(range(0, 10))