# -*- coding: utf-8 -*-
"""
list 특징
- 1차원 배열 구조
- 형식: 변수 = [x1, x2, x3, ..., n]
- 다양한 자료형 저장 가능
- index 사용(순서 존재)

@author: wonseok
"""

# 단일 list + index
lst = [1, 2, 3, 4, 5]
print(lst)

for i in lst:
#    print(i, end = (' '))
    print(lst[i-1:])

for i in lst:
    print(lst[:i])

x = list(range(1, 101))
print(x[:5]) # 0 ~ 4
print(x[-5:])

print(x[::2]) # 홀수
print(x[1::2]) # 짝수

# 중첩 list + index
a = ['a', 'b', 'c'] # 단일 lsit
print(a, type(a)) # ['a', 'b', 'c'] <class 'list'>

b = [10, 20, a, True, '문자열'] # [[]] 중첩 리스트
print(b)

print(b[2]) # a 참조
print(b[2][1]) # a의 두번째 원소

# 3. 추가, 삽입, 수정, 삭제
num = ['one', 'two', 'three', 'four']
print(len(num))

num.append('five') # five 추가
num.remove('five') # five 삭제

num[3] = '4' # 값 수정
print(num, len(num))

num.insert(0, 'zero')

# list 연산: 결합, 확장, 추가, 곱셈
x = [1, 2, 3, 4]
y = [1.5, 2.5]

# list 결합
z = x + y

# list 확장
x.extend(y) # x 확장: 기존 object에 원소만 추가.

# list 추가
x.append(y) # x에 추가 - y의 객체 그 자체가 추가됨.

# list 반복 ( * )
lst * 2 # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# list 사칙연산: list 객체 대상 사칙연산 불가
# ex) lst * 0.5 -> Error !

lst.sort(reverse = True)
lst

lst.clear() # 전체 원소 제거


# scala vs vector

vector = []
size = int(input('vector size: '))
print(size)

for i in range(size): # 0 ~ 4
    vector.append(i + 10)

print(vector) # [10, 11, 12, 13, 14]


# list에서 원소 찾기
# if 'element' in list:
    # run

'''
리스트 내포: list + for
- list에서 for문 사용
형식1) 변수 = [실행문 for]
'''

x = [2, 4, 1, 5, 7]

lst = []
for i in x:
    print(i ** 2)
    lst.append(i**2)

lst

lst2 = [i ** 2 for i in x] # https://redmuffler.tistory.com/452
lst2

# 변수 = [실행문 for if]
# 1 ~ 100 사이에서 5의 배수 호출
num = list(range(1, 101))
print(num)

num2 = [i for i in num if 1 % 5 == 0]
print(num2)

num2 = [i for i in num if 1 % 5 == 0]

a = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
print(len(a))

a_sum = [sum(i) for i in a]
print(a_sum) # [6, 60, 600]


# 얕은 복사, 깊은 복사
names = ['홍길동', '이순신', '유관순']

# 얕은 복사 -> 메모리 주소가 같다
names2 = names # 주소 복사
print(id(names), id(names2))

# 깊은 복사 -> 메모리 주소가 다르다
names_copy = names.copy()
print(id(names), id(names_copy))
print(names, names2, names_copy)

# 원본 내용 변경
names[0] = 'kong'
print(names, names2, names_copy)
# ['kong', '이순신', '유관순'] ['kong', '이순신', '유관순'] ['홍길동', '이순신', '유관순']
