# -*- coding: utf-8 -*-
"""
step01_groupby.py

- 집단변수(범주형)를 이용한 자료처리 

1. 집단변수 기준 subset 만들기 
2. 집단변수 기준 group & 통계량 
3. group & 통계량 시각화 
"""

import pandas as pd
import os

os.chdir('C:/ITWILL/4_Python-II/data')

# dataset load & 변수 확인 
wine = pd.read_csv('winequality-both.csv')
print(wine.info())
'''
RangeIndex: 6497 entries, 0 to 6496
Data columns (total 13 columns):
 0   type                  6497 non-null   object : 집단변수 
   :
 12  quality               6497 non-null   int64 : 와인 품질 
''' 

# 칼럼 공백 -> "_" 교체 
wine.columns = wine.columns.str.replace(' ', '_')
wine.head()

# 5개 변수 선택 -> subset 
wine_df = wine.iloc[:, [0,1,4,11,12]]
wine_df.info()
'''
RangeIndex: 6497 entries, 0 to 6496
Data columns (total 5 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   type            6497 non-null   object 
 1   fixed_acidity   6497 non-null   float64
 2   residual_sugar  6497 non-null   float64
 3   alcohol         6497 non-null   float64
 4   quality         6497 non-null   int64
'''

# 칼럼명 수정 : 2가지(전체 수정, 부분 수정)
#wine_df.columns = ['a','b','c','d','e'] 

# 부분 수정 
columns = {'fixed_acidity':'acidity',
           'residual_sugar':'sugar'} # {'old','new'}

wine_df = wine_df.rename(columns = columns)
wine_df.info()

# 집단변수 확인 : 와인 유형 
wine_df.type.unique() # 유일값 확인 : ['red', 'white']
wine_df['type'].value_counts() # 범주 빈도수 
'''
white    4898
red      1599
'''

# 집단변수 확인 : 와인 품질 
wine_df['quality'].unique()
# [5, 6, 7, 4, 8, 3, 9] -> 명칭(label) 해석 

wine_df['quality'].value_counts()

wine_df.shape # (6497, 5)

# 1. 집단변수 기준 subset 만들기 

# 1) type 기준 : 특정 칼럼 조건식 subset 
red_wine = wine_df[wine_df['type'] == 'red']
red_wine.shape # (1599, 5) : 2d
red_wine.head()

white_wine = wine_df[wine_df.type == 'white']
white_wine.shape # (4898, 5) : 2d
white_wine.head()

# 2) 특정 칼럼 선택  
wine_red_quality = wine_df.loc[wine_df['type'] == 'red', 
                               'quality']
wine_red_quality.shape # (1599,) : 1d

wine_red_quality

wine_white_quality = wine_df.loc[wine_df['type'] == 'white',
                                 'quality']
wine_white_quality.shape # (4898,) : 1d
wine_white_quality


# 2. 집단변수 기준 group & 통계량

# 1) 집단변수 1개 이용 그룹화 
# 형식) DF.groupby('집단변수')

type_grp = wine_df.groupby('type') # 그룹객체 
print(type_grp) # GroupBy object

# 그룹 빈도수 
type_grp.size()
'''
red      1599
white    4898
'''

# 그룹 객체 구성 
for grp in type_grp : 
    print(type(grp))
    print(grp)

'''
<class 'tuple'> : ('red', DF)
<class 'tuple'> : ('white', DF)
'''

# 그룹객체 -> 특정 그룹 추출 
red_wine = type_grp.get_group('red')
red_wine.shape # (1599, 4)
white_wine = type_grp.get_group('white')
white_wine.shape # (4898, 4)


# 각 그룹별 통계 
type_grp.sum()
type_grp.mean()
# 평균 : white wine 알콜, 품질 우수 


# 2) 집단변수 2개 이상 그룹화
# 형식) DF.groupby(['집단변수1', '집단변수2'])
wine_grp = wine_df.groupby(['type', 'quality']) 
# 2 * 7 = 최대 14개 집단  

# 그룹별 빈도수 
wine_grp.size()

# 그룹별 통계 
wine_grp.mean()

# 와인의 유형에 따른 품질의 빈도수 
wine_grp.size().shape # (13,) -1d

# 1d -> 2d : reshape(type:행, quality:열) 
wine_grp_2d = wine_grp.size().unstack() 
wine_grp_2d
wine_grp_2d.shape # (2, 7) - 2d


# 3. group & 통계량 시각화
import matplotlib.pyplot as plt 

# 차트에서 한글 지원 : c:\windows\fonts
plt.rcParams['font.family'] = 'HYGothic-Extra'#'Malgun Gothic'#malgun.ttf

# 와인의 유형에 따른 품질의 빈도수 
wine_grp_2d.plot(kind = 'barh', stacked=True,
                 title='와인의 유형에 따른 품질')
plt.show()


# 그룹 통계 시각화 
wine_mean = wine_grp.mean()

# 고품질 와인 : 대체적으로 설탕 적고, 알콜 높음 
wine_mean[['sugar', 'alcohol']].plot(kind='bar')
plt.show()













      
    