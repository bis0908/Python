# -*- coding: utf-8 -*-
"""
step02_DataFrame.py

DataFrame 자료구조 특징 
 - 2차원 행렬구조(DB의 table 구조와 유사함)
 - 칼럼 단위 상이한 자료형 
 - DataFrame 칼럼 = Series(1차원)
"""

import pandas as pd # pd.DataFrame()
from pandas import DataFrame # DataFrame()


# 1. DataFrame 생성 

# 1) 기본 자료구조(list, dict) 이용 
name = ['hong', 'lee', 'kim', 'park'] 
age = [35, 45, 55, 25]
pay = [250, 300, 350, 200]

# {'key':value} -> key : 칼럼명, value : 값 
data = {'name':name, 'age':age, 'pay':pay} # dict

frame = pd.DataFrame(data, columns=['name','age','pay'])
print(frame)
'''
   name  age  pay
0  hong   35  250
1   lee   45  300
2   kim   55  350
3  park   25  200
'''
frame.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 0   name    4 non-null      object -> string 
 1   age     4 non-null      int64 
 2   pay     4 non-null      int64    
'''

# DF 칼럼 추가 : Series 객체 이용 
gender = pd.Series(['M','F','M','F']) # 1차원 

frame['gender'] = gender
print(frame)
'''
   name  age  pay gender
0  hong   35  250      M
1   lee   45  300      F
2   kim   55  350      M
3  park   25  200      F
'''

names = frame.name # frame.col
print(names)
type(names) # pandas.core.series.Series

# 2) numpy 객체 이용 
import numpy as np # 별칭 

frame2 = DataFrame(np.arange(12).reshape(3,4),
                   columns=['a','b','c','d'])
print(frame2)
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''
frame2.info()
frame2.shape # (3, 4)

# 행/열 통계 구하기 
frame2.mean(axis = 0) # 행축(default) : 열단위 평균 
frame2.mean(axis = 1) # 열축 : 행단위 평균 
'''
행축 : 같은 열들의 모음 
열축 : 같은 행들의 모음 
'''

# 3) csv file 이용 
import os 
os.chdir('C:/ITWILL/4_Python-II/data')

emp = pd.read_csv('emp.csv', encoding='utf-8')
print(emp.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   No      5 non-null      int64 
 1   Name    5 non-null      object
 2   Pay     5 non-null      int64 
'''

print(emp)

# 2. DF 칼럼 참조 

# 1) 단일 칼럼 : DF.column or DF['column']
emp.No # DF.column
emp['Pay'] # DF['column']
 
emp['Pay'].plot()

# 2) 복수 칼럼 : [[]] - 중첩list
emp[['No','Pay']].plot()

col = ['No','Name'] # list
emp[col]


# 3. subset 만들기 : old DF -> new DF

# 1) 특정 칼럼 제외 
subset1 = emp[['Name', 'Pay']]
print(subset1)

# 2) 특정 행 제외 
subset2 = emp.drop(0) # 1행 제거 
print(subset2)

# 3) 조건식 이용 : 특정 칼럼 값 기준 
# 형식) DF[조건식] : 급여 350 초과 수령자 
subset3 = emp[emp.Pay > 350]
print(subset3)

# 4) columns 이용 
print(emp.columns) # ['No', 'Name', 'Pay']
 
iris = pd.read_csv('iris.csv')
print(iris.info())
'''
 0   Sepal.Length  150 non-null    float64
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64
 3   Petal.Width   150 non-null    float64
 4   Species       150 non-null    object 
'''

# DF.column or DF['column']
#iris.Sepal.Length # error : 점이 포함된 칼럼명 

iris['Sepal.Length']

# 칼럼명을 list 추출 
cols = list(iris.columns)
print(cols) # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

cols[:4] # x : ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
cols[-1] # y : 'Species'

# x변수 
x_iris = iris[cols[:4]]
# y변수 
y_iris = iris[cols[-1]] # iris['Species']

x_iris.shape # (150, 4) - 2d
y_iris.shape # (150,) - 1d


# 4. DataFrame 행열 참조 
'''
DF.loc[row, col] : primarily label based : 명칭 기반 
DF.iloc[row, col] : primarily integer position based : 위치 기반 
'''

print(emp)
'''
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
[열이름] -> 명칭(label) 기반 
[행이름] -> 위치기반(integer position) 기반 
'''

# 1) loc 속성 : 명칭 기반 
# DF.loc[행label, 열label]
emp.loc[0, :] # 1행 전체 
emp.loc[0] # 1행 전체(생략 : 열 전체) 
emp.loc[0:3] # 4행 전체 
# 숫자 -> 명칭으로 해석 

emp.loc[:,'Name':'Pay'] # 연속 칼럼 
emp.loc[:,['No','Pay']] # 비연속 칼럼 

# 2) iloc 속성 : 위치 기반 
# DF.iloc[integer, interger]
emp.iloc[0, :] # 1행 전체
emp.iloc[0]
emp.iloc[0:3] # 3행 

emp.iloc[:, 1:] # 연속 칼럼 
emp.iloc[:, [0, 2]] # 비연속 칼럼 
emp.iloc[[0,2,4], [0, 2]] # 행렬 비연속 칼럼 

# TypeError
#emp.iloc[:,'Name':'Pay']









