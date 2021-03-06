# -*- coding: utf-8 -*-
"""
step02_apply.py

1. group 객체 대상 외부함수 적용
   - DF.apply(func), DF.agg([f1, f2])
2. data 정규화    
"""

import pandas as pd
import seaborn as sn 


iris = sn.load_dataset('iris')
iris.info()


# 1. group 객체 대상 외부함수 적용

# 1) 1개 칼럼만 그룹 객체 
iris_grp = iris['sepal_length'].groupby(iris['species'])

# 그룹 빈도수 
iris_grp.size()
'''
setosa        50
versicolor    50
virginica     50
'''

# 사용자 정의함수 
def avg(group) :
    return group.mean()

def diff(group) :
    return group.max() - group.min()

# 2) DF.apply(func)
iris_grp.apply(sum) # biltin
'''
setosa        250.3
versicolor    296.8
virginica     329.4
'''
iris_grp.apply(max) # biltin
iris_grp.apply(min) # biltin
iris_grp.mean() # DF.mean()
iris_grp.apply(avg) # apply(사용자정의함수)
iris_grp.apply(diff) # apply(사용자정의함수)


# 3. DF.agg([f1, f2, ...])
agg_func = iris_grp.agg(['sum','max','min', avg, diff])

agg_func.plot(kind='barh')


# 2. data 정규화 : 변수의 값을 일정한 범위로 조정 
from numpy import min, max # max, min

# 1) 사용자정의함수 : data 정규화(0~1) 
def normal(x) :
    nor = (x - min(x)) / (max(x) - min(x))
    return nor 

    
x = [100, 2000, 50000, 5]
print(normal(x)) # 함수 호출 
# [0.00190019 0.03990399 1.         0.        ]


df = iris.iloc[:, :4]
df_nor = df.apply(normal)

df.head() # 정규화 전 
df_nor.head() # 정규화 후 




