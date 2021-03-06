# -*- coding: utf-8 -*-
"""
step03_pivot_table

@author: wonseok
"""

import pandas as pd
import os

os.chdir('E:\Code\Python\itwill\python-2\data')
pivot = pd.read_csv('pivot_data.csv')
pivot.info()

 # 0   year     8 non-null      int64
 # 1   quarter  8 non-null      object
 # 2   size     8 non-null      object
 # 3   price    8 non-null      int64

table = pd.pivot_table(data = pivot, values = 'price', index = ['year', 'quarter'],
                       columns = 'size', aggfunc = 'sum')
table
