# -*- coding: utf-8 -*-
"""
list 특징 
 - 1차원 배열 구조 
   형식) 변수 = [값1, 값2, ... n]
 - 다양한 자료형 저장 가능 
 - index 사용(순서 존재) : 변수[index]
 - 값 수정(추가,삽입,수정,삭제)
"""

# 1. 단일 list + index 
lst = [1,2,3,4,5] # lst = list([1,2,3,4,5])
print(lst) # [1, 2, 3, 4, 5]

for i in lst :
    #print(i, end = ' ') # 1 2 3 4 5 
    print(lst[i-1:]) # i-1 ~ n

for i in lst :
    print(lst[:i]) # 0~i-1
    
'''
처음/마지막(최근) 데이터 추출 
'''    
x = list(range(1,101)) # 1 ~ 100
print(x)

print(x[0])
# 처음 5개 원소 참조 
print(x[:5])
# 마지막(최근) 5개 원소 참조 
print(x[-5:])

'''
2씩 증가 index
'''
print(x[:]) # 전체 원소 [start:stop]
print(x[::2]) # [start:stop:step] : 홀수 
print(x[1::2]) # [start:stop:step] : 짝수 

# list 합
print("x의 전체합 =", sum(x))


# 2. 중첩 list + index
a = ['a', 'b', 'c'] # 단일 list 
print(a, type(a), len(a)) # ['a', 'b', 'c'] <class 'list'> 3


b = [10, 20, a, True, '문자열'] # [[]] : 중첩 list
print(b) # [10, 20, ['a', 'b', 'c'], True, '문자열']

print(b[2]) # a 참조 
print(b[2][1])  # a의 2번째 원소 


# 3. 추가,삽입,수정,삭제
num = ['one', 'two', 'three', 'four']
print(len(num)) # 4

num.append('five') # 추가 
print(num, len(num))
# ['one', 'two', 'three', 'four', 'five'] 5

num.remove('five') # 삭제 
print(num, len(num))
# ['one', 'two', 'three', 'four'] 4


num[3] = '4' # 수정 : index 이용 
print(num, len(num)) # ['one', 'two', 'three', '4'] 4

num.insert(0, 'zero') # 삽입 
print(num, len(num)) # ['zero', 'one', 'two', 'three', '4'] 5

# exam01_1.py


# 4. list 연산 : 결합(+), 확장, 추가, 반복(*)    

x = [1, 2, 3, 4]
y = [1.5, 2.5]

# 1) list 결합(+)
z = x + y # new object 
print(z) # [1, 2, 3, 4, 1.5, 2.5]

# 2) list 확장 
x.extend(y) # x 확장 : 기존 object - 원소 추가 : 단일 list 
print(x) # [1, 2, 3, 4, 1.5, 2.5]

# 3) list 추가 
x.append(y) # x 추가 : 기존 object - 객체 추가 : 중첩 list
print(x) # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]

# 4) list 반복(*) 
print(lst) # [1, 2, 3, 4, 5]
result = lst * 2
print(result) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
 
# list 사칙연산 : list 객체 대상 사칙연산 불가 
#lst * 0.5 # TypeError

lst_mul = [] # 곱셈 저장 
for i in lst :
    print(i * 0.5) # 콘솔 출력 
    lst_mul.append(i * 0.5) # list 저장 
    
print(lst_mul)


# 5. list 멤버 
# dir(object) : object의 멤버 확인 
type(result) # list

dir(result) # count, pop, sort, clear

# object.member() = method 
result.count(5) # 해당 원소 개수 반환 
result.pop(0) # index 원소 추출 & 제거 : 1
print(result) # [2, 3, 4, 5, 1, 2, 3, 4, 5]

result.sort() # (key, reverse) : 오름차순 정렬 
print(result)

result.sort(reverse= True) # 내림차순 정렬 
print(result)

result.clear() # 전체 원소 제거 
print(result) # []


# 6. scala vs vector 
'''
scala 변수 : 한 개의 값(상수)를 갖는 변수(크기)
vector 변수 : 다수의 값을 갖는 변수(크기와 방향)
'''

vector = [] # 빈 list 
size = int(input('vector size : ')) # scala 변수 
print(size)

for i in range(size) : # 0 ~ 4
    vector.append(i+10) # vector 변수 
    
print(vector)


# 7. list에서 원소 찾기 
'''
if '원소' in list :
    실행문 
'''

import random # 난수 생성 

r = [] # 빈 list
for i in range(10) :
    r.append(random.randint(1, 5))  # 1~5난수 정수 

if 4 in r :
    print('4가 있음')
else :
    print('4가 없음')

print('r : ', r)

# exam01_2, exam01_3







