﻿'''
step01  문제
'''

'''
문) 다음과 같이 수량과 단가 변수를 만들어서 금액을 출력하시오.

 조건1) 수량 변수 : su = 5
 조건2) 단가 변수 : dan = 800
 조건3) 수량과 단가 변수 :  주소 확인 
 조건4) 금액(price) = 수량 * 단가 


<<화면출력 예시>>
su 주소 : 1858560352
dan 주소 : 2241324818224
금액 = 4000
'''

su = 5
dan = 800
price = su * dan

print('su 주소 : ', id(su))
print('dan 주소 : ', id(dan))
print('금액 = ', price)

