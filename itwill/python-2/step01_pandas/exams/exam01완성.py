''' 
step02 관련문제 
문1) score.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> tv 칼럼이 0인 관측치 2개 삭제 (조건식 이용)
   조건2> score, academy 칼럼만 추출하여 DataFrame 생성
   조건3> score, academy 칼럼의 평균 계산 
   - <<출력 결과 >> 참고    
   
<<출력 결과 >>
   score  academy
1     75        1
2     77        1
3     83        2
4     65        0
5     80        3
6     83        3
7     70        1
9     79        2
score      76.500
academy     1.625   
'''

import pandas as pd
import os
os.chdir("c:/ITWILL/4_Python-II/data") # file 경로 변경 

score = pd.read_csv('score.csv')

# 조건1> tv 칼럼이 0인 관측치 2개 삭제 (조건식 이용)
subset = score[score.tv != 0] 
print(subset)

# 조건2> score, academy 칼럼만 추출하여 DataFrame 생성
df = score[['score', 'academy']] # 복수 칼럼 선택 
print(df)

# 조건3> score, academy 칼럼의 평균 계산 
print(df.mean(axis = 0)) # 행축 : 열단위 평균 









