# -*- coding: utf-8 -*-
"""
step02_operator_print.py

연산자와 print()
 1. 할당 연산자(=) : 변수에 값 할당
 2. 연산자 : 산술,논리,관계연산자
 3. print() : 표준출력장치 - 콘솔 출력
 4. input() : 표준입력장치 - 키보드 입력
 5. 형변환(casting) : 자료형 변환
"""

# 1. 할당 연산자(=) : 변수에 값 할당
i = tot = 0
#sum = 0 - 사용금지

i += 1 # i = i + 1 : 카운터 변수
tot += i # tot = tot + i # 누적 변수
print("i=", i) # i= 1
print("tot=", tot) # tot= 1

# 서로 다른값 할당
var1, var2 = 100, 200
print(var1, var2) # 100 200

# 값 교체(swap)
var2, var1 = var1, var2
print(var1, var2) # 200 100

# 패킹(packing) 할당
lst = [1,2,3,4,5] # vector 변수
print(len(lst)) # 5

v1, *v2 = lst
print(v1, v2) # 1 [2, 3, 4, 5]
'''
v1 : scala 변수 - 0차원
v2 : vector 변수 - 1차원
'''

*v1, v2 = lst
print(v1, v2) # [1, 2, 3, 4] 5


# 2. 연산자 : 산술,관계,논리 연산자

num1 = 10 # 피연산자1
num2 = 21 # 피연산자2

# 산술연산자
add = num1 + num2
print('add=', add) # add= 120

div = num1 / num2
print('div=', div) # div= 5.0

div = num1 // num2 # 정수 반환
print('div=', div) # div= 5

div2 = num1 % num2
print('div2=', div2) # div2= 0

exp = num1 ** num2 # power
print('exp=', exp)

# 관계 연산자
# (1) 동등비교
bool_re = num1 == num2 # False
bool_re2 = num1 != num2 # True
print(bool_re, bool_re2) # False True

# (2) 대소비교(>, >=, <, <=)
print(num1 >= num2) # True
print(num1 < num2) # False

# 논리 연산자 : and, or, not
bool_re = num1 > num2 and num1 == num2
print('and =', bool_re) # and = False

bool_re = num1 > num2 or num1 == num2
print('or =', bool_re) # or = True

print(not(num1 <= num2)) # False -> True


# 3. print() : 표준출력장치 - 콘솔 출력
help(print) # 함수 도움말
# Help on built-in function print in module builtins:
# 내장 모듈 소속 - 내장함수

'''
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
'''

# 1) value 인수
print("value =", 10+20)

# 2) sep 인수
print("010","111","1111", sep='-') # 010-111-1111

# 3) end 인수
print("이름 : ", end=' ') # 같은줄에 중복 출력
print("홍길동") # 이름 :  홍길동

# 4) %양식문자 : ppt.23
# 형식) print('%양식문자' %값 )
num1, num2 = 10, 20
num3 = num1 + num2

print('%d + %d = %d' %(num1, num2, num3)) # 10진수 정수
print('원주율 = %8.3f'%(3.14159)) # 원주율 =    3.142 : 10진수 실수
# 전체 50%가 90점 이상이다.
print('전체 %d%%가 %d점 이상이다.'%(50, 90))
print("이름 : %s"%("홍길동")) # 문자열

# 5) format() 함수
# 형식1) print('{}'.format(값)))
print("이름은 {}이고, 나이는 {}이다.".format("홍길동", 35))
print("이름은 {1}이고, 나이는 {0}이다.".format(35, "홍길동"))

# 형식2) print('{번호:format}'.format(값)))
print("정수 : {0:d}, {1:5d}".format(12, 345)) # 정수 : 12,   345
print("천단위 콤마 : {0:3,d}".format(123456)) # 천단위 콤마 : 123,456
print('원주율 = {0:.3f}'.format(3.14159)) # 원주율 = 3.142

# 형식3) print('{번호:방향}'.format(값))) : > 오른쪽, < 왼쪽
print('원주율1 = {0:>8.3f}, 원주율2 = {1:<8.3f}'.format(3.14159, 3.14159))
# 원주율1 =    3.142, 원주율2 = 3.142


# 축약형
name = "홍길동"
age = 35
print(f"이름은 {name}이고, 나이는 {age} 입니다.")

# SQL문 작성
sql = f"select * from emp name = '{name}'"
print(sql) # select * from emp name = '홍길동'

#############################
### exam02_1, exam02_2
#############################


# 4. input() : 표준입력장치 - 키보드 입력
n1 = int(input('첫번째 숫자 입력 : ')) # 문자열 -> 숫자 정수형
n2 = float(input('두번째 숫자 입력 : ')) # 문자열 -> 숫자 실수형

print(n1 + n2) # 30


# 5. 형 변환(casting) : 자료형 변환
print(int(25.45)) # 실수 -> 정수

#int('Hello') # ValueError
print(2 + int('10')) # 산술연산자 : 문자열 -> 정수
print('나이 =', 35) # 나이 = 35
print('나이 =' + str(32)) # 결합연산자 : 나이 =32

# 논리형(T/F) -> 정수형(1/0)
print(int(True)) # 1
print(int(False)) # 0

# 정수형(1/0) -> 논리형(T/F)
print(bool(5)) # True
print(bool(0)) # False

#######################
### exam02_3
#######################















