# -*- coding: utf-8 -*-
"""
step03_DF_reshape.py

DataFrame 모양 변경 
"""
import pandas as pd 
import os 

os.chdir('C:\\ITWILL\\4_Python-II/data')
buy = pd.read_csv('buy_data.csv')
print(buy.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Date         22 non-null     int64
 1   Customer_ID  22 non-null     int64
 2   Buy          22 non-null     int64
'''

# 모양 확인 
buy.shape # (22, 3) : 2차원 
buy.head()

# 1. wide(2차원) -> long(1차원)
buy_long = buy.stack() # 22 * 3 = 66
buy_long.shape # (66,) : 1차원 

# 2. long(1차원) -> wide(2차원)
buy_wide = buy_long.unstack()
buy_wide.shape # (22, 3)

# 3. 전치행렬 
buy_tran = buy.T
buy_tran.shape # (3, 22)

# 4. 중복 행 제거 
print(buy)
buy.duplicated() # 중복 행 여부 반환 
buy2 = buy.drop_duplicates() # 중복 행 게거 
buy2.shape # (20, 3)

# 5. 특정 칼럼을 index 지정 
new_buy = buy.set_index('Date')
new_buy.columns # ['Customer_ID', 'Buy']

new_buy.shape # (22, 2)


new_buy.loc[20150101]
new_buy.loc[20150104]







