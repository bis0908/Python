'''
step04, 05 문제

 문1) 중복 되지 않은 직위와 각 직위별 빈도수를 출력하시오.

 <<출력 결과 >>
 중복되지 않은 직위 : ['사장', '과장', '대리', '부장']
 각 직위별 빈도수 : {'과장': 2, '부장': 1, '대리': 2, '사장': 1}
'''

position = ['과장', '부장', '대리', '사장', '대리', '과장']
cnt = {}

for ch in position:
    if ch in cnt: # cnt에 ch가 있는 경우
        cnt[ch] += 1
    else: # cnt에 ch가 없는 경우
       cnt[ch] = 1 # value 초기화

key = cnt.keys()

key.sort(reverse = True)

print('중복되지 않은 직위: {}'.format(cnt.keys()))
print('각 직위별 빈도수: {}'.format(cnt))
