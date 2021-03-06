'''
 카이제곱 검정(chisquare test)
  - 확률변수 X의 적합성 검정 - 일원
  - 두 집단변수 간의 독립성 검정 - 이원
  - 검정통계량(기대비율) = sum( (관측값 - 기댓값)**2 / 기댓값 )
  - 검정통계량 채택역 : -1.96 ~ +1.96
'''

from scipy import stats # 확률분포 검정


# 1) 일원 chi-square(1개 변수 이용) : 적합성 검정
# 귀무가설 : 관측치와 기대치는 차이가 없다.
# 대립가설 : 관측치와 기대치는 차이가 있다.

real_data = [4, 6, 17, 16, 8, 9] # 관측치
exp_data = [10,10,10,10,10,10] # 기대치
chis = stats.chisquare(real_data, exp_data)
chis    # statistic=14.200000000000001, pvalue=0.014387678176921308
print('statistic = %.3f, pvalue = %.3f'%(chis))
# statistic = 14.200, pvalue = 0.014




# 2) 이원 chi-square(2개 변수 이용) : 교육수준과 흡연 간의 독립성 검정
#귀무가설 : 교육수준과 흡연율 간에 관련성이 없다.(채택)
#연구가설 : 교육수준과 흡연율 간에 관련성이 있다.(기각)

# 파일 가져오기
import pandas as pd
import os
os.chdir('E:\Code\Python\itwill\python-2\data')

smoke = pd.read_csv("smoke.csv")

# <단계 1> 변수 선택
print(smoke)# education, smoking 변수
education = smoke.education # x 변수
smoking = smoke.smoking # y변수


# <단계 2> 교차분할표
tab = pd.crosstab(index=education, columns=smoking)
print(tab)


#<단계 3> 카이제곱 검정
statistic, pvalue = stats.chisquare(education, smoking)
print('statistic = %.3f, pvalue = %.3f'%(statistic, pvalue))





