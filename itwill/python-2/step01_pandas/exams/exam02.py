'''
step02 관련문제
문2) wdbc_data.csv 파일을 읽어와서 단계별로 x, y 변수를 생성하시오.
     단계 1 : 파일 가져오기, 정보 확인
     단계 2 : y변수 : diagnosis
              x변수 : id 칼럼 제외  나머지 30개 칼럼
'''
import pandas as pd
import os
os.chdir('E:\Code\Python\itwill\python-2\data') # file 경로 변경

# 단계 1 : 파일 가져오기, 정보 확인

wbdc = pd.read_csv('wdbc_data.csv', encoding = 'utf-8')
print(wbdc)
# 단계 2 : y변수, x변수 선택

cols = list(wbdc.columns)
print(cols)

x_var = wbdc[cols[2:]]
y_var = wbdc[cols[1]]

x_var.shape
y_var.shape

