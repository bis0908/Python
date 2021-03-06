# -*- coding: utf-8 -*-
"""
step03_DF_LinearRegression.py

DataFrame(csv file) + 회귀모델 
"""

import pandas as pd # csv file read
from sklearn.linear_model import LinearRegression # model 
from sklearn.metrics import mean_squared_error, r2_score # 평가도구 
from sklearn.model_selection import train_test_split # split


# 1. dataset load
path = 'C:/ITWILL/4_Python-II/data/' # file path 

iris = pd.read_csv(path + 'iris.csv')
print(iris.info())

# 2. 변수 선택 
'''
formula = y(3) ~ x(1,2,4)
'''
cols = list(iris.columns)
cols
# ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

y_col = cols.pop(2) # 3칼럼 추출 & 제외 
y_col # 'Petal.Length'

x_cols = cols[:-1]
x_cols # ['Sepal.Length', 'Sepal.Width', 'Petal.Width']

X = iris[x_cols] # 중첩list 
y = iris[y_col] # 단일list

X.shape # (150, 3)
y.shape # (150,)

# 3. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)


X_train.shape # (105, 3)
X_test.shape # (45, 3)


# 4. model 생성 : train set 
lr = LinearRegression()

model = lr.fit(X_train, y_train)

model.coef_ # [ 0.75572271, -0.6715641 ,  1.43222782]


# 5. model 평가 : test set 
y_pred = model.predict(X = X_test)


mse = mean_squared_error(y_true = y_test, y_pred = y_pred)
print(mse) # 0.12397491396059161

score = r2_score(y_true = y_test, y_pred = y_pred)
print(score) # 0.9643540833169766

# 과적합 유무 확인 
model.score(X_train, y_train) # 0.9694825528782403
model.score(X_test, y_test) # 0.9643540833169766
'''
[해설] 두 점수 결과 비슷함 : 과적합 없음 
test set -> validation set  : 검증용 
'''

# 6. model 적용 : new dataset(업무용)
import numpy as np 

idx = np.random.choice(len(iris), int(len(iris)*0.5), replace=False)
idx
len(idx) # 75

new_data = iris.iloc[idx]

new_X =  new_data[x_cols]
new_y = new_data[y_col]

new_y_pred = model.predict(new_X)

score = r2_score(new_y, new_y_pred)
print(score) # 0.9611722654785116











