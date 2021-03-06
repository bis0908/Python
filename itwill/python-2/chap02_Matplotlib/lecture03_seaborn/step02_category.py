# -*- coding: utf-8 -*-
"""
step02_category

@author: wonseok
"""

import matplotlib.pyplot as plt
import seaborn as sb

# 1. dataset load
tips = sb.load_dataset('tips')
tips.info()
type(tips) # pandas.core.frame.DataFrame: D.F이므로 관련 함수 호출 가능함

#  2   sex         244 non-null    category
#  3   smoker      244 non-null    category
#  4   day         244 non-null    category
#  5   time        244 non-null    category

ttn = sb.load_dataset('titanic')
ttn.info()

ttn['sex'].unique()     # object
ttn['class'].unique()   # category

'''
object vs category
공통점: 문자열형
object: 셀 수 없는 문자열
category: 셀 수 있는 문자열 (범주형)
'''

# 2. 범주형 category 변수 시각화
sb.countplot('smoker', data = tips)     # 2개 범주
plt.title('smoker of tips')

sb.countplot('class', data = ttn)   # 3개 범주
plt.title('class of titanic')

sb.countplot('day', data = tips)   # 4개 범주
plt.title('day of tips')