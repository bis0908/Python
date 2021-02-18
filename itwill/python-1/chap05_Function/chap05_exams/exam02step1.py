'''
문2-1) 다음 벡터(emp)는 '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하는 함수를 정의하시오.

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''

from re import findall
from re import sub

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# 함수 정의
def name_pro(emp):
    names = [sub('[0-9]', '', t) for t in emp]
    return names

# 함수 호출
names = name_pro(emp)
print('names =', names)





