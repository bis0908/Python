# -*- coding: utf-8 -*-
"""
step02_apply

1. group 객체 대상 외부함수 적용
    - DF.apply(func), DF.agg()

2. data 정규화
@author: wonseok
"""

import pandas as pd
import seaborn as sn

iris = sn.load_dataset('iris')
iris.info()

# 1. group 객체 대상 외부함수 적용

# 1.1 1개 칼럼만 그룹 객체 만들기
iris['sepal_length'].groupby('species')