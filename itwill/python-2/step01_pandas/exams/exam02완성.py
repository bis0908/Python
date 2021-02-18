'''
step02 관련문제
문2) wdbc_data.csv 파일을 읽어와서 단계별로 x, y 변수를 생성하시오.
     단계 1 : 파일 가져오기, 정보 확인 
     단계 2 : y변수 : diagnosis 
              x변수 : id 칼럼 제외  나머지 30개 칼럼
'''
import pandas as pd
import os
os.chdir("c:/ITWILL/4_Python-II/data") # file 경로 변경 

# 단계 1 : 파일 가져오기, 정보 확인 
wdbc = pd.read_csv('wdbc_data.csv')
print(wdbc.info())
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
'''

# 단계 2 : y변수, x변수 선택
cols = list(wdbc.columns)

y_wdbc = wdbc[cols[1]]
y_wdbc.shape # (569,)

x_wdbc = wdbc[cols[2:]]
x_wdbc.shape # (569, 30)










    
