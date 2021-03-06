# -*- coding: utf-8 -*-
"""
step01_groupby

- 집단변수(범주형)를 이용한 자료처리

1. 집단변수 기준 subset 만들기
2. 집단변수 기준 group & 통계량
3. group & 통계량 시각화

@author: wonseok
"""
import pandas as pd
import os
os.chdir('E:\Code\Python\itwill\python-2\data')

wine = pd.read_csv('winequality-both.csv')
wine.info()

# column 공백 -> '_'
wine.columns = wine.columns.str.replace(' ', '_')
wine.head()

# 5개 변수 선택 -> subset
wine_df = wine.iloc[:, [0, 1, 4, 11, 12]]
wine_df.info()
# RangeIndex: 6497 entries, 0 to 6496
# Data columns (total 5 columns):
#      Column          Non-Null Count  Dtype
# ---  ------          --------------  -----
#  0   type            6497 non-null   object
#  1   fixed_acidity   6497 non-null   float64
#  2   residual_sugar  6497 non-null   float64
#  3   alcohol         6497 non-null   float64
#  4   quality         6497 non-null   int64

# 칼럼명 수정: 2가지 방법 (전체 수정 or 부분 수정)
# wine_df.columns = ['a', 'b', 'c', 'd', 'e']

# 부분 수정 -> {'old': 'new'}
columns = {'fixed_acidity': 'acidity', 'residual_sugar': 'sugar'}

wine_df = wine_df.rename(columns = columns)

# 집단변수
wine_df.type.unique() # ['red', 'white']
wine_df['type'].value_counts()
# white    4898
# red      1599

# 집단변수 확인: 와인 품질
wine_df['quality'].unique() # [5, 6, 7, 4, 8, 3, 9] -> 명칭(label) 해석
wine_df['quality'].value_counts()

# 1. 집단변수 기준 subset 만들기
# 1.1 type 기준: 특정 칼럼 조건식 subset
red_wine = wine_df[wine_df['type'] == 'red']
red_wine.shape # (1599, 5)

white_wine = wine_df[wine_df.type == 'white']
white_wine.shape # (1599, 5)

# 1.2 특정 칼럼 선택
red_wine_quality = wine_df.loc[wine_df['type'] == 'red', 'quality']
red_wine_quality.shape

white_wine_quality = wine_df.loc[wine_df['type'] == 'white', 'quality']
white_wine_quality.shape


# 2. 집단변수 기준 group & 통계량
# 형식) DF.groupby('집단변수')

type_grp = wine_df.groupby('type')

# 그룹 빈도수
type_grp.size()

# 그룹 객체 구성
for grp in type_grp:
    print(type(grp))
    print(grp)

# 그룹 객체 -> 특정 그룹 추출
red_wine = type_grp.get_group('red')
red_wine.shape      # (1599, 5)

white_wine = type_grp.get_group('white')
white_wine.shape    # (4898, 5)

# 각 그룹별 통계
type_grp.sum()
type_grp.mean()
# 평균: white wine 알콜, 품질 우수

# 2.2 집단변수 2개 이상 그룹화
# DF.groupby(['집단변수1', '집단변수2'])
wine_grp = wine_df.groupby(['type', 'quality'])

wine_grp.size()

# 그룹별 빈도수
wine_grp.mean()

# 와인의 유형에 따른 품질의 빈도수
wine_grp.size().shape # (13, )

# 1d -> 2d: reshape(type: row, quality: column)
wine_grp_2d = wine_grp.size().unstack()
wine_grp_2d
wine_grp_2d.shape


# 3. group & 통계량 시각화
import matplotlib.pyplot as plt
# 차트에서 한글 지원 : c:\windows\fonts
plt.rcParams['font.family'] = 'D2coding' #malgun.ttf

# 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False


wine_grp_2d.plot(kind = 'barh', stacked = True, title = '와인의 유형에 따른 품질')

# 그룹 통계 시각화
wine_mean = wine_grp.mean()

wine_mean[['sugar', 'alcohol']].plot(kind = 'bar')
