# -*- coding: utf-8 -*-
"""
step01_slope_intercept

y = (X * slope) + intercept

slope = Cov(x, y) / Sxx(x의 편차 제곱의 평균)
        Cov(X, Y) = sum((X - xmu) * (Y - ymu)) / n
        Sxx = mean((x - xmu) ** 2)

intercept = ymu - (slope * xmu)

@author: wonseok
"""

from scipy import stats
import pandas as pd
import os
os.chdir('E:\Code\Python\itwill\python-2\data')

galton = pd.read_csv('galton.csv')
galton.info()

x = galton.parent # 독립변수(입력변수)
y = galton.child # 종속변수(결과변수)

model = stats.linregress(x, y)
model
# =============================================================================
# LinregressResult(slope=0.646290581993639,
#                  intercept=23.941530180412975,
#                  rvalue=0.45876236829282113,
#                  pvalue=1.7325092920168095e-49,
#                  stderr=0.04113588223793343)
# =============================================================================


# 기울기와 절편 구하기
# slope = Cov(x, y) / Sxx(x의 편차 제곱의 평균)

# x, y 산술평균
xmu = x.mean()
ymu = y.mean()

# 공분산: 모집단
# Cov(X, Y) = sum((X - xmu) * (Y - ymu)) / n
Cov = sum((x - xmu) * (y - ymu)) / len(x)
Cov # 2.062389686756837

import numpy as np

Sxx = np.mean((x - xmu) ** 2)
slope = Cov / Sxx
slope # 0.6462905819936413

# 절편
intercept = ymu - (slope * xmu)
intercept # 23.94153018041171

# 설명력: rvalue
rvalue = x.corr(y)
rvalue # 0.45876236829282124

R_squared = rvalue ** 2
R_squared # 0.21046291056163816
