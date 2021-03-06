'''
t검정 : t 분포에 대한 가설검정  
t분포 : 모집단 정규분포, 사례수(d.f=n-1)가 30개 미만 분포 
z분포 : 모집단 정규분포, 사례수가 30개 이상 분포

t 검정 유형 
  1. 한 집단 평균 검정
  2. 두 집단 평균 검정
  3. 대응 두 집단
'''

from scipy import stats # test
import numpy as np # sampling
import pandas as pd # csv file read

# 1. 한 집단 평균 검정 : 남자 평균 키(모평균) : 175.5cm -> 29명 표본추출 
sample_data = np.random.uniform(172,179, size=29) 
print(sample_data)
print(len(sample_data),'명') 

# 기술통계 
print('평균 키 =', sample_data.mean()) # np.mean

# 단일집단 평균차이 검정 
statistic, pvalue = stats.ttest_1samp(sample_data, 175.5) 

print('t검정 통계량 = %.3f, pvalue = %.5f'%(statistic, pvalue))
# t검정 통계량 = 0.570, pvalue = 0.57307
# 채택역 : -1.96 ~ 1.96
# 해설 : 남자 평균 키에 차이가 없다. 


# 2. 두 집단 평균 검정 : 남여 평균 점수 차이 검정 
female_score = np.random.uniform(50, 100, size=30) # 여성 
male_score = np.random.uniform(45, 95, size=30) # 남성 

two_sample = stats.ttest_ind(female_score, male_score)
print(two_sample)
print('두 집단 평균 차이 검정 = %.3f, pvalue = %.3f'%(two_sample))


# file 자료 이용 : 교육방법에 따른 실기점수 평균차이 검정 
sample = pd.read_csv('c:/itwill/4_python-ii/data/two_sample.csv')
print(sample.info())

two_df = sample[['method', 'score']]
print(two_df)

# 교육방법 기준 subset
method1 = two_df[two_df.method==1] # 방법1 
method2 = two_df[two_df.method==2] # 방법2 

# score 칼럼 추출 
score1 = method1.score
score2 = method2.score

# NA -> 평균대체 
score1 = score1.fillna(score1.mean())
score2 = score2.fillna(score2.mean())

# 두 집단 평균차이 검정 
two_sample = stats.ttest_ind(score1, score2)
print(two_sample)
'''
Ttest_indResult(statistic=-0.9468624993102985, 
                pvalue=0.34466920341921115)
'''

# 3. 대응 두 집단 : 복용전 65 -> 복용후 60 몸무게 변환  
before = np.random.randint(60, 65, size=30)  
after = np.random.randint(59, 64,  size=30) 

paired_sample = stats.ttest_rel(before, after)
print(paired_sample)
print('t검정 통계량 = %.5f, pvalue = %.5f'%paired_sample)
# t검정 통계량 = 3.49583, pvalue = 0.00154

# pvalue < alpha(0.05) : 몸무게 변환 있음 

# 두 집단 평균 
before.mean() # 62.63333333333333
after.mean() # 61.266666666666666

diff = before.mean() - after.mean()
print('평균차이 = ', diff) # 평균차이 = 1.3666666666666671








