# -*- coding: utf-8 -*-
"""
step04_csvFileIO.py

1. csv file read
2. read data 처리 
3. csv file write
"""
import pandas as pd 
import os 

os.chdir('C:\\ITWILL\\4_Python-II/data')

# 1. csv file read

# 1) 칼럼명이 없는 경우 
st = pd.read_csv('student.csv', header=None)
st #      0     1    2   3

# 칼럼명 수정 
col_names = ['sno','name','height','weight']
st.columns = col_names

print(st)

# 2) 칼럼명 특수문자(.) or 공백 
iris = pd.read_csv('iris.csv')
print(iris.info())

# DF.['column']

iris.columns = iris.columns.str.replace('.','_')
iris.info() # Sepal_Length
iris.Sepal_Length

# 3) 특수구분자, 천단위 콤마 
# pd.read_csv('file', delimiter='\t', thousands=',')


# 2. read data 처리 : 파생변수 
print(st)
'''
비만도 지수(BMI)
BMI = 몸무게/(키**2)
몸무게 단위 : KG
키 단위 : CM -> M
'''
175 * 0.01 # 1.75

BMI = st['weight'] / (st['height']*0.01)**2
BMI

# 파생변수1 추가 
st['BMI'] = BMI
st

# label = 정상 : 18~23 or '비만' or '저체중'

label = []
for bmi in st.BMI :
    if bmi >= 18 and bmi <= 23 :
        label.append('정상')
    elif bmi > 23 :
        label.append('비만')
    else:
        label.append('저체중')
        
# 파생변수2 추가 
st['label'] = label      
print(st)        
        
    
# 3. csv file write
type(st) # pandas.core.frame.DataFrame

# index = None : 행 이름 제외 
st.to_csv('st_info.csv', index = None, encoding='utf-8')

st2 = pd.read_csv('st_info.csv', encoding='utf-8')
print(st2)






















