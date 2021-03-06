# -*- coding: utf-8 -*-
"""
step01_descriptive_statistics

- 기술 통계 관련 함수: 대표값, 산포도

@author: wonseok
"""

import statistics as st
import pandas as pd
import os

os.chdir('E:\Code\Python\itwill\python-2\data')

data = pd.read_csv('descriptive.csv')
data.info()

# 변수 선택
x = data['cost']
x[:10]

# 1. 대표값
x.mean()

lst = x.to_list() # pandas 객체 -> list 객체로
lst

st.mean(lst)

st.mean(x)
st.median(x)
st.median_low(x)
st.median_high(x)
st.mode(x)

x.value_counts()

# 2. 산포도: 분산, 표준편차
var = st.variance(x)
var

std = st.stdev(x)
std

std2 = st.sqrt(var)
std2


