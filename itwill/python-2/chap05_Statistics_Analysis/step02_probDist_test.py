# -*- coding: utf-8 -*-
"""
step02_probDist_test.py

확률분포와 검정(test)
 - 확률분포 : 확률 + 자료분포 
   ex) 동전 1,000번 시행 -> 앞(1) or 뒷(0) 확률 
 - 가설검정 : 유의확률(통계모델) vs 유의수준(alpha=0.05) 
    ex) pvalue = 0.08 >= alpha=0.05(신뢰수준:95%=1-alpha)

1. 연속확률분포 : 정규분포,균등분포,카이제곱, Z/T/F분포 
    - 정규분포와 검정    
2. 이산확률분포 : 베르누이분포, 이항분포, 포아송분포 
    - 이항분포와 검정 
"""

from scipy import stats # 확률분포와 검정 
import numpy as np # 수치 처리 
import matplotlib.pyplot as plt  # 확룰분포의 시각화 


# 1. 정규분포와 검정(정규성 검정)

# 1) 표준정규분포 객체 생성 
mu, sigma = 0, 1 # 평균, 표준편차 
norm_obj = stats.norm(mu, sigma) # object
print(norm_obj) # object info

# 2) 확률변수 X
N = 1000 # sample 수  
X = norm_obj.rvs(size = N) # N번 시뮬레이션 
print(X)

# 확률밀도함수 : 확률밀도분포곡선 추가 
from scipy.stats import norm # 확률밀도 함수 

# 분포곡선 vector data 
vec = np.linspace(start=min(X), stop=max(X), num=100)
len(vec) #  100   
 
# 3) 확률분포에 시각화 
plt.hist(X, bins='auto', density=True) # 히스토그램 
plt.plot(vec, norm.pdf(vec, mu, sigma), color='red') 
#확률밀도분포곡선 추가 
plt.show()

# 4) 정규성 검정 
# 귀무가설(H0) : 정규분포와 차이가 없다.(o)
# 대립가설(H1) : 정규분포와 차이가 있다.

print(stats.shapiro(X))
'''
ShapiroResult(statistic=0.9980834722518921, pvalue=0.31938084959983826)
'''

statistic, pvalue = stats.shapiro(X)
print('검정통계량 : ', statistic)
print('유의확률 : ', pvalue)
'''
검정통계량 :  0.9980834722518921
유의확률 :  0.31938084959983826
'''

alpha = 0.05 # 채택 or 기각 

if pvalue >= alpha :
    print('귀무가설 채택 ')
else :
    print('귀무가설 기각 ') # 대립가설 채택 
    
# 귀무가설 채택

# 2. 이항분포와 검정 
'''
이항분포 : 이항변수(2가지 범주)를 갖는 확률분포(성공=1 or 실패=0) 
 - 베르누이분포 : 이항변수에서 성공(1)이 나올 확률분포 
 - 이항분포 : 베르누이 시행을 통해서 얻은 확률분포
    B(1, p) : 베르누이분포 
    B(n, p) : 이항분포     
'''

# 1. 표본 추출 

# 1) 동전 확률실험 : 독립시행 : n, 성공확률 : p=0.5

# - 독립시행 n=1, 성공확률 = p : 베르누이분포 모집단 -> 표본(10) 
sample1 = stats.binom.rvs(n=1, p=0.5, size=10)
print(sample1) # [1 1 1 1 0 1 1 0 1 0]

# - 독립시행 n=5, 성공확률 = p : 이항분포 모집단 -> 표본(10)
sample2 = stats.binom.rvs(n=5, p=0.5, size=10)
print(sample2) # [1 2 3 3 3 4 4 3 3 3]

#  2) 주사위 확률실험 : 독립시행 : n, 성공확률 : p = 1/6 -> 표본(10)
sample3 = stats.binom.rvs(n=6, p=1/6, size=10)
print(sample3) # [2 0 2 0 0 1 0 2 2 1]


# 2. 이항검정 : 이항분포에 대한 가설 검정 
'''
연구환경 : 게임에 이길 확률이 40%이고, 게임의 시행횟수가 100일때 
           95% 신뢰수준 이항검정 
귀무가설 : 게임에 이길 확률은 40%와 차이가 없다. 
대립가설 : 게임에 이길 확률은 40%와 차이가 있다. 
'''

# 1) 베르누이 분포 -> 표본(100개) 추출 
# B(1, p=0.4)
n = 1 # 독립시행 
p = 0.4 # 모수 

X = stats.binom.rvs(n=n, p=p, size=100)
print(X)

# 2) 성공회수 카운터 
cnt = np.count_nonzero(X)
print('성공회수 =', cnt) # 성공회수 = 41

# 3) 이항검정 
help(stats.binom_test)
# binom_test(x, n=None, p=0.5, alternative='two-sided')
# x : 성공회수, n : 시행회수, p : 귀무가설 성공확률, alternative : 양측검정)   
n = 100 # size
pvalue = stats.binom_test(x=cnt, n=n, p=0.4, alternative='two-sided')
# 0.8388931714011669

# 유의확률 vs 유의수준(alpha)
alpha = 0.05 # 알파 결정 : 0.95 = 1-alpha

if pvalue >= alpha :
    print('귀무가설 채택')
else :
    print('귀무가설 기각')


#######################
## 이항검정 example
#######################

'''
150명의 합격자 중에서 남자 합격자가 62명 일때 
99% 신뢰수준에서 남여 합격률에 차이가 있다고 
볼 수 있는가?

귀무가설 : 남여 합격률에 차이가 없다.(p=0.5) 
'''

cnt = 62 # 성공회수 
n = 150 # 시행회수 

pvalue = stats.binom_test(x=cnt, n=n, p=0.5, alternative='two-sided')

alpha = 0.01 # 0.99 = 1 - alpha

if pvalue >= alpha :
    print('남여 합격률에 차이가 없다.')
else :
    print('남여 합격률에 차이가 있다.')

# 남여 합격률에 차이가 없다.



