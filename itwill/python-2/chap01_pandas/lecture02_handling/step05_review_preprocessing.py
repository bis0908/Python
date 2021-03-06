# -*- coding: utf-8 -*-
"""
step05_review_preprocessing.py

 - 네이버 영화 리뷰 데이터 참고
 - 영화 리뷰 텍스트 전처리
"""

import pandas as pd # csv file, 전처리
import os # file path

# 1. file read
os.chdir('E:\Code\Python\itwill\python-2\data')

'''
pd.read_csv() : 콤마 구분자
pd.read_table() : 특수문자(\t, :, ;, 공백)
'''
review_df = pd.read_table('naver_movie_review.txt')
print(review_df.info())
'''
RangeIndex: 35237 entries, 0 to 35236
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   id      35237 non-null  int64 - 사용자 구분
 1   review  35233 non-null  object - 감상평
 2   label   35237 non-null  int64 - yes(1) or no(0)
'''

# 2. dataset 확인
review_df.head()
review_df.tail()

# 칼럼 유일값/빈도수 확인
review_df['id'].nunique() # 35237
review_df['label'].nunique() # 2
review_df['label'].unique() # [1, 0]

# label 빈도수
review_df['label'].value_counts()
'''
1    17751
0    17486
'''

review_df['review'].nunique() # 34694
35233 - 34694 # 539 중복확인


# 3. dataset 전처리

# 1) 전처리1 : 중복제거
review_df.drop_duplicates(subset='review', inplace=True)
'''
subset='칼럼' : 칼럼으로 중복 제거 -> subset 생성
inplace=True : 현재 객체 결과 반영
'''

review_df.shape # (34695, 3)
35237 - 34695 # 542

# 2) 전처리2 : review 대상 - 영문, 숫자, 특수문자 등 제거
review_df['review'][:10] # review 10개
# 파생변수 생성
review_df['review2'] = review_df['review'].str.replace("[^가-힣|' ']","")

review_df.info()
'''
 0   id       34695 non-null  int64
 1   review   34694 non-null  object
 2   label    34695 non-null  int64
 3   review2  34694 non-null  object
'''
# 정제 전 vs 정제 후
review_df['review'][:10]
review_df['review2'][:10]


# 3) 전처리3 : NaN -> ''(null) : 결측치 처리
import numpy as np

review_df['review2'].replace('', np.nan, inplace=True)

# 전체 칼럼 결측치 확인
review_df.isnull() # True/False

# 결측치 제거
new_df = review_df.dropna()

new_df.info()
'''
 0   id       34525 non-null  int64
 1   review   34525 non-null  object
 2   label    34525 non-null  int64
 3   review2  34525 non-null  object
 '''
34694 - 34525 # 169

new_df['review2'][:10]





