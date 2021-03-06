# -*- coding: utf-8 -*-
"""
step02_sklearn_LinearRegression.py
"""

from sklearn.datasets import load_diabetes, load_iris # function 
from sklearn.linear_model import LinearRegression # model 
from sklearn.metrics import mean_squared_error, r2_score # 평가도구 
from sklearn.model_selection import train_test_split # split

######################
## diabetes
######################

# 1. dataset loading 
X, y = load_diabetes(return_X_y=True) # 입력, 정답 

X.shape # (442, 10) : 2d
y.shape # (442,) : 1d

type(X) # numpy.ndarray

# 2. 변수 특징 분석 
# x변수 : 정규화(o) 
X.mean() # -1.6638274468590581e-16
X

# y변수 : 정규화(x)
y


# 3. train/test split(70 : 30)
idx = int(len(X) * 0.7) # 309

X_train = X[:idx] # X[:idx, :]
X_test = X[idx:] # X[idx:, :] 

X_train.shape # (309, 10) - 훈련셋 
X_test.shape # (133, 10) - 검정셋 

y_train = y[:idx] # 훈련셋
y_test = y[idx:] # 검정셋 

# 4. model 생성 
lr = LinearRegression() # 생성자 -> object 

model = lr.fit(X=X_train, y=y_train) # 지도학습  

# member 확인 
dir(model) # coef_, intercept_, predict, score

print('기울기 =', model.coef_)
print('절편 =', model.intercept_)


# 5. model 평가 
y_pred = model.predict(X=X_test) # 검정셋-예측치 
y_true = y_test # 관측치(정답)


# 1) MSE : 정규화(O)
MSE = mean_squared_error(y_true, y_pred)
print('MSE =', MSE) # MSE = 2722.170821603729
'''
error = y_true - y_pred
squared = error**2
mean(squared)
'''

# 2) 결정계수 : 정규화(x)
score = r2_score(y_true, y_pred)
print('r2 score =', score) # r2 score = 0.5172474671249085


# 3) score() 메서드 
score_train = model.score(X=X_train, y=y_train)
score_test = model.score(X=X_test, y=y_test)
print('train core =', score_train)
# train core = 0.5117388684800468
print('test core =', score_test)
# test core = 0.5172474671249085


######################
## iris
######################

# 1. dataset load
iris = load_iris()

X = iris.data
y = iris.target 

# 2. 변수 특징 
X.shape # (150, 4) : 2d
y.shape # (150,) : 1d

X
y # class(0,1,2)

# 3. train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state = 123)

X_train.shape # (105, 4) - 70%
X_test.shape # (45, 4) - 30%

X_train
X_test


# 4. model 생성 
lr2 = LinearRegression() # 생성자 -> object 

model2 = lr2.fit(X=X_train, y=y_train) # 지도학습 

dir(model2)

model2.coef_ # [-0.12562409, -0.04786676,  0.24405498,  0.5730085 ]
model2.intercept_ # 0.25025520367096055


# 5. model 평가 
y_pred = model2.predict(X_test) # 예측치 
y_true = y_test # 정답 

# 1) MSE : 0수렴 정도 
mse = mean_squared_error(y_true, y_pred)
print('MSE = ', mse) # MSE =  0.04473327237231242

error = y_true - y_pred # 오차 
squared_error = error**2  # 1. 부호 절대값, 2. 패널티 
mean_squared_error = squared_error.mean() # 전체 관측치 평균 
print('MSE = ', mean_squared_error) # MSE =  0.04473327237231242

# 2) r2 score : 1수렴 정도 
score = r2_score(y_true, y_pred)
print('score =', score) # score = 0.9424492525070314

# 3) score : 모델의 과적합 확인 
model2.score(X_train, y_train) # 0.9219438937692478
model2.score(X_test, y_test) # 0.9424492525070314




