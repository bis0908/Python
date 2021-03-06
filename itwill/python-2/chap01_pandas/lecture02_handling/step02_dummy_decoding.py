# -*- coding: utf-8 -*-
"""
step02_dummy_decoding.py

dummy(one hot encoding) vs decoding 
1. 집단변수를 x변수로 사용
   - 범주값이 다항인 경우 
   ex) x[a=1, b=0, c=0] -> y 영향도 
2. 집단변수를 y변수로 사용 
   - 다항분류 : model 분류 
   - 분류 결과 : decoding
"""

import pandas as pd 


music = pd.DataFrame({'id':[1,2,3,4,5],
                      'genre':['rock','dicso','pop','rock','pop']},
                     columns = ['id', 'genre'])
music

music['genre'].value_counts()
'''
rock     2
pop      2
dicso    1
'''

# 1) dummy(one hot encoding) : 2진 표현(1 or 0)
dummy = pd.get_dummies(data = music['genre']) 
print(dummy)
'''
   dicso  pop  rock <- genre
0      0    0     1
1      1    0     0
2      0    1     0
3      0    0     1
4      0    1     0
'''
type(dummy) # pandas.core.frame.DataFrame

# 칼럼 단위 결합 
music_df = pd.concat(objs= [music, dummy], axis = 1) # cbind
music_df


# 2) decoding : 10진수(2진수 -> 10진수)
import numpy as np 

# pandas obj -> numpy obj 
arr = np.array(dummy)
type(arr) # numpy.ndarray
print(arr)
'''
[[0 0 1] - 2
 [1 0 0] - 0
 [0 1 0] - 1
 [0 0 1] - 2
 [0 1 0]]- 1
'''

arr.shape # (5, 3)

decoding = np.argmax(arr, 1)
decoding # [2, 0, 1, 2, 1]

# 칼럼 추가 
music_df['decoding'] = decoding
print(music_df)
'''
   id  genre  dicso  pop  rock  decoding
0   1   rock      0    0     1         2
1   2  dicso      1    0     0         0
2   3    pop      0    1     0         1
3   4   rock      0    0     1         2
4   5    pop      0    1     0         1
'''















