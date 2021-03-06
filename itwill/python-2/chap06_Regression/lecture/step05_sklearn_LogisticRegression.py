# -*- coding: utf-8 -*-
"""
step05_sklearn_LogisticRegression.py

 - y변수 범주형인 경우
 - 활성함수 유형
 - 이항 분류기 : sigmoid function
 - 다항 분류기 : softmax functoin
"""

from sklearn.datasets import load_breast_cancer, load_iris # dataset
from sklearn.linear_model import LogisticRegression # model
from sklearn.metrics import accuracy_score, confusion_matrix # 평가 도구
from sklearn.model_selection import train_test_split # split
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sn # heatmap - Accuracy Score

############################
## 1. binary class
############################

# 1. dataset loading
cancer = load_breast_cancer()

X = cancer.data
y = cancer.target

X.shape # (569, 30)
X
y.shape
y # 0(양성) or 1(악성)


# 2. model 생성
help(LogisticRegression)
'''
C=1.0, random_state=None,
solver='lbfgs',max_iter=100,multi_class='auto'

1. C=1.0 : cost function -> 값이 크면 : 복잡한 훈련(정확도 높고, 과대적합)
2. random_state=None : 난수 seed값 지정
3. solver='lbfgs' : 최적화 이용되는 알고리즘
 solver : {'newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'},             default='lbfgs'
 'lbfgs' : 일반데이터셋
 'sag', 'saga' : 빅데이터셋
4. max_iter=100 : 기본 반복횟수
5. multi_class='auto' : 다항분류 : multinomial
   multi_class : {'auto', 'ovr', 'multinomial'}, default='auto'
'''

obj = LogisticRegression(random_state=0)
model = obj.fit(X, y)

# 분류정확도 : 훈련셋 기준
score = model.score(X, y)
print('score =', score) # score = 0.9472759226713533


y_pred = model.predict(X)
y_pred # 0 or 1

# 교차분할표
import pandas as pd

tab = pd.crosstab(y, y_pred)
print(tab)
'''
col_0    0    1
row_0
0      193   19
1       11  346
'''
type(tab) # pandas.core.frame.DataFrame

acc = (tab.iloc[0,0] + tab.iloc[1,1]) / len(y)
print('accuracy =', acc)
# accuracy = 0.9472759226713533

# 평가도구
acc = accuracy_score(y, y_pred)
print('accuracy =', acc)
# accuracy = 0.9472759226713533


############################
## 2. multi-class
############################

# 1. dataset loading
X, y = load_iris(return_X_y=True)


# 2. model 생성
obj = LogisticRegression(random_state=0,
                         solver='lbfgs',
                         multi_class='multinomial')

model = obj.fit(X, y)

# 예측치: class vs 확률 값
y_pred = model.predict(X)
y_pred2 = model.predict_proba(X)
y_pred2 # [9.81798885e-01, 1.82011004e-02, 1.43499227e-08]
sum([9.81798885e-01, 1.82011004e-02, 1.43499227e-08]) # 0.9999999997499227

y_pred.shape (150, )

# 교차분할표
tab = pd.crosstab(index=y, columns=y_pred)
print(tab)
'''
col_0   0   1   2
row_0
0      50   0   0
1       0  47   3
2       0   1  49
'''

acc = accuracy_score(y_true=y, y_pred=y_pred)
print('accuracy =', acc)
# accuracy = 0.9733333333333334

acc = (tab.iloc[0,0] + tab.iloc[1,1] + tab.iloc[2,2]) / len(y)
print('accuracy =', acc)

# 혼돈 행렬(confusion_matrix)
con_max = confusion_matrix(y, y_pred)
print(con_max)
'''
[[50  0  0]
 [ 0 47  3]
 [ 0  1 49]]
'''

score = model.score(X, y)
print('score =', score)
# score = 0.9733333333333334

import matplotlib.pyplot as plt
import seaborn as sn # heatmap - Accuracy Score

# confusion matrix heatmap
plt.figure(figsize=(6,6)) # chart size
sn.heatmap(con_max, annot=True, fmt=".3f", linewidths=.5, square = True); # , cmap = 'Blues_r' : map »ö»ó
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(score)
plt.title(all_sample_title, size = 18)
plt.show()


# =============================================================================
# digits: multi-class
# =============================================================================
from sklearn.datasets import load_digits

digits = load_digits()

X_img = digits.data
y_lab = digits.target

X_img.shape # (1797, 64) -> 64(8, 8)
X_img.max() # 16.0
X_img.min() # 0.0

y_lab.shape # (1797,) -> 10진수(0 ~ 9)

# 색인과 내용 넘기기
lst = [1, 2, 3, 4, 5]
lst2 = [2, 3, 4, 5, 6]

for i, (c1, c2) in enumerate(zip(lst, lst2)):
    print(i, c1, c2)

# 5개 이미지 출력
import matplotlib.pyplot as plt

plt.figure(figsize = (10, 4))

for idx, (img, lab) in enumerate(zip(X_img[:5], y_lab[:5])):
    plt.subplot(1, 5, idx + 1)
    plt.imshow(img.reshape(8, 8), cmap = 'gray') # image
    plt.title('image: %d'%(lab), fontsize = 20)

plt.show()

# 75% vs 25%
X_train, X_test, y_train, y_test = train_test_split(X_img, y_lab, random_state=123) # test_size=0.25
X_train.shape # (1347, 64)


# model 생성
obj = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')

model = obj.fit(X_train, y_train) # 100번 반복학습: 1347 * 100

# model 평가
y_pred = model.predict(X_test) # y class

score = accuracy_score(y_true = y_test, y_pred = y_pred)
score # 0.9644444444444444

con_max = confusion_matrix(y_true = y_test, y_pred = y_pred)
con_max



# confusion matrix heatmap

plt.figure(figsize=(6,6)) # chart size
sn.heatmap(con_max, annot=True, fmt=".3f", linewidths=.5, square = True);# , cmap = 'Blues_r' : map »ö»ó
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(score)
plt.title(all_sample_title, size = 18)
plt.show()