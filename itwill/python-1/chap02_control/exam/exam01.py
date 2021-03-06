'''
step01 관련 문제

A형 문) 항공사에서는 짐을 부칠 때, 10kg 이상이면 수수료 10,000원을 지불해야 한다.
     만약 10kg 미만이면 수수료는 없다. 사용자의 짐의 무게를 키보드로 입력 받고,
     사용자가 지불해야 할 금액을 계산하는 프로그램을 작성하시오.

<출력 예시>
짐의 무게는 얼마입니까? 8
수수료는 없습니다.

짐의 무게는 얼마입니까? 15
수수료는 10,000원 입니다.


B형 문) 항공사에서는 짐을 부칠 때, 10kg 이상 부터 수수료를 지불해야 한다.
     수수료는 10의 배수 단위로 10,000원씩 증가한다.
     만약 10kg 미만이면 수수료는 없다.
     사용자의 짐의 무게를 키보드로 입력 받고, 사용자가 지불해야 할
     금액을 계산하는 프로그램을 작성하시오.

<출력 예시>
짐의 무게는 얼마입니까? 8
수수료는 없습니다.

짐의 무게는 얼마입니까? 15
수수료는 10,000원 입니다.

짐의 무게는 얼마입니까? 21
수수료는 20,000원 입니다.
'''

weight = int(input('짐의 무게는 얼마입니까? (단위: kg): '))
price = 10000
if weight >= 10:
    fee = weight//10 * price
    print('수수료는 {0:,}원 입니다.'.format(fee))
else:
    print('수수료는 없습니다.')