# -*- coding: utf-8 -*-
"""
step02_while

반복문(while)

형식)
while 조건식 : 
    실행문
    실행문 
    
loop : 조건식 = True일때 실행문     
"""


# 카운터, 누적변수 
cnt = tot = 0 # 초기화 

while cnt < 5 :    
    cnt += 1 # cnt = cnt + 1
    print('cnt = ', cnt)
    tot += cnt # tot = tot + cnt
    print('tot =', tot)

# 1 ~ 100까지 합, 5의 배수의 합 
cnt = tot = 0 # 초기화 
while cnt < 100 :
    cnt += 1 # cnt = cnt + 1
    
    # 5의 배수인 경우 
    if cnt % 5 == 0 :
        print(cnt, end= ' ') # 5의 배수 원소 
        tot += cnt # tot = tot + cnt
    
#print('1~100까지 합 =', tot) # 1~100까지 합 = 5050
print('\n1~100까지 5의 배수의 합 =', tot)

# 문) 1~100 사이에서 5의 배수이면서(and) 3의 배수가 아닌 합 계산하기 
cnt = tot = 0 # 초기화 
while cnt < 100 :
    cnt += 1 # cnt = cnt + 1
    
    # 5의 배수인 경우 
    if cnt % 5 == 0 and cnt % 3 != 0 :
        print(cnt, end= ' ') # 5의 배수 원소 
        tot += cnt # tot = tot + cnt
    
print('\ntot = %d'%(tot))


# 무한 loop -> 종료 조건 필요함 
while True :
    num = int(input('숫자 입력 : '))
    
    if num == 0 : # 종료 조건 
        print('프로그램 종료')
        break # loop exit 
    
    print("입력 값 : ", num)


'''
숫자 맞추기 게임 : 1 ~ 10
myinput == computer : '성공' -> exit
myinput > computer : '더 작은 수 입력'
myinput < computer : '더 큰 수 입력'
'''

print('>> 숫자 맞추기 게임 <<')

import random # 난수 생성 모듈 

com = random.randint(1, 10) # 1 ~ 10 난수 정수 

while True :
    myinput = int(input('예상 숫자를 입력해봐 : '))
    if myinput == com :
        print('~~ 성공 ~~ ')
        break # loop exit 
    elif myinput > com :
        print('~~ 더 작은 수 입력 ~~ ')
    else :
        print('~~ 더 큰 입력 ~~ ')
        
        
'''
break, continue
 - break : loop 탈출 
 - continue : 계속 반복, 다음 문장 skip  
'''

i = 0 # 초기화 
while i < 10 :
    i += 1 # 카운터 변수 
    
    if i % 2 != 0 :
        continue # 다음 문장 skip
    if i > 6 :
        break # exit
        
    print(i, end=' ') # 1 3 5 -> 2 4 6
    
















