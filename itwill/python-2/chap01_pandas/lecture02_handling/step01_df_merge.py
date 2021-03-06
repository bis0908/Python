# -*- coding: utf-8 -*-
"""
step01_DF_merge.py

1. DF 병합(merge)
   ex) DF1(id) + DF2(id) = DF3
2. DF 결합(concat)
   ex) DF1 + DF2 = DF3
3. inner join vs outer join
"""

import pandas as pd 
import os 

os.chdir('C:\\ITWILL\\4_Python-II/data')

wdbc = pd.read_csv('wdbc_data.csv')
wdbc.info()
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
'''

cols = list(wdbc.columns)
len(cols) # 32

# DF1(16) + DF2(16)
DF1 = wdbc[cols[:16]] # 16
DF1.shape # (569, 16)
DF2 = wdbc[cols[16:]] # 16
DF2.shape # (569, 16)

# 1. DF 병합(merge)
DF2['id'] = wdbc.id
DF2.shape # (569, 17)

DF3 = pd.merge(left=DF1, right=DF2, on='id') # how = inner
DF3.shape # (569, 32)
DF3.info()

# 2. DF 결합(concat)
DF2 = wdbc[cols[16:]]
DF2.shape # (569, 16)

DF4 = pd.concat(objs=[DF1,DF2], axis = 1) # cbind
DF4.info()


# 3. inner join vs outer join
name = ['hong','lee','park','kim']
age = [35, 20, 33, 50]

df1 = pd.DataFrame(data = {'name':name, 'age':age}, 
                   columns = ['name', 'age'])

df1


name2 = ['hong','lee','kim']
age2 = [35, 20, 50]
pay = [250, 350, 250]

df2 = pd.DataFrame(data = {'name':name2, 'age':age2,'pay':pay}, 
                   columns = ['name', 'age', 'pay'])

df2

inner = pd.merge(left=df1, right=df2, how='inner')
inner
'''
   name  age  pay
0  hong   35  250
1   lee   20  350
2   kim   50  250
'''

outer = pd.merge(left=df1, right=df2, how='outer')
outer
'''
   name  age    pay
0  hong   35  250.0
1   lee   20  350.0
2  park   33    NaN -> 결측치 
3   kim   50  250.0
'''




