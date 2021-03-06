# -*- coding: utf-8 -*-
"""
step04_scaling_LinearRegression.py

data scaling(정규화 or 표준화) : 이물질 제거 
 - 특징변수(x변수)의 값에 따라서 model 영향을 미치는 경우 적용 
    ex) 범죄율(-0.01~0.99), 주택가격(99~999)
 - 정규화 : 변수의 값을 일정 범위로 조정(0~1, -1~+1) : X변수 
 - 표준화 : 표준화 공식 Z이용(평균=0, 표준편차=1) : Y변수 
           Z = (X - mu) / sigma
"""

from sklearn.datasets import load_boston # dataset 
from sklearn.model_selection import train_test_split # split 
from sklearn.linear_model import LinearRegression # model 
from sklearn.metrics import mean_squared_error, r2_score # 평가 

from sklearn.preprocessing import minmax_scale # 정규화(0~1)-X변수 
from scipy.stats import zscore # 표준화(mu=0, st=1)-Y변수 
import numpy as np # 난수 

X = np.random.randint(0, 100, (5, 4)) # 0~99
X

X_nor = minmax_scale(X)
'''
x - min(x) / max(x) - min(x)
'''
X_nor.shape # (5, 4)
X_nor.min() # 0
X_nor.max() # 1

# 1. dataset load 
X, y = load_boston(return_X_y=True)

X.mean() # 70.07396704469443


# 2. X, y변수 스케일링 
X_nor = minmax_scale(X) # X변수 스케일링 
X_nor.shape # (506, 13)

X_nor.mean() # 0.3862566314283195

y.mean() # 22.532806324110677

y_nor = zscore(y) # mu=0, st=1 - y변수 스케일링 
type(y_nor) # numpy.ndarray
'''
z = (x - mu) / sigma 
'''
y_nor.mean() # -5.195668225913776e-16
y_nor.std() # 0.9999999999999999


# 3. train/test split : 75% vs 25%
X_train, X_test, y_train, y_test = train_test_split(
    X_nor, y_nor, random_state=123) # test_size=0.25


X_train.shape # (379, 13)
X_test.shape #  (127, 13)


# 4. model 생성 : train set 
lr = LinearRegression()

model = lr.fit(X_train, y_train)

model.coef_ # 13


# 5. model 평가 : test set 
y_pred = model.predict(X = X_test)


mse = mean_squared_error(y_true = y_test, y_pred = y_pred)
print(mse) # 0.29339802406435306

score = r2_score(y_true = y_test, y_pred = y_pred)
print(score) # 0.6862448857295742







