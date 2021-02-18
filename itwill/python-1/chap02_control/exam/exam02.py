'''
step02 관련 문제

문) 다음과 같이 아메리카노 3잔만 제공하는 커피 자판기를 구현하시오.
     (커피 한 잔은 2500원이라고 가정한다.)
     조건1> 2500원 미만, 금액이 부족합니다. 반복 수행
     조건2> 2500원 이상, 맛있게 드세요. 잔돈 표시, 커피 잔 빼기
     조건3> 2500원 이면, 맛있게 드세오. 커피 잔 빼기
     조건4> 커피 3잔을 모두 판매하면 프로그램 종료
'''
import time

print("==" * 15)
time.sleep(1)
print('아메리카노 커피 자판기 동작')
time.sleep(1)
print('가격은 2,500원')
time.sleep(1)
print('커피는 3잔만 판매 가능')
time.sleep(1)
print("==" * 15)
time.sleep(1)

coffee = 3 # 커피 3잔


while True: # 무한 반복
    coin = int(input('동전 혹은 지폐를 투입 해주세요: '))

    if coin < 2500:
        print('금액이 부족합니다.')
        time.sleep(1)
        print('잔돈이 배출됩니다. 잔액: {}'.format(coin))


    elif coin >= 2500:
        time.sleep(2)
        coin -= 2500
        print('\n커피 만드는 중...')
        time.sleep(2)
        print('''커피가 나왔습니다! \n잔여 coffee 수량: {}\n잔돈이 배출됩니다.
              잔액: {}\n'''.format(coffee-1, coin))
        time.sleep(2)
        coffee -= 1

    if coffee == 0: # 종료 조건
        time.sleep(2)
        print('~~ 죄송합니다. 커피 재고가 소진되어 더 이상 자판기를 사용하실 수 없습니다. ~~')
        time.sleep(2)
        print('잔돈이 배출됩니다. 잔액: {}'.format(coin))
        break
