# -*- coding: utf-8 -*-
"""
step05_Dictionary

dict 특징
- set 자료구조와 유사함
- 비 순서 자료 구조
형식) 변수: {key:value, key2:value2, ..., n}
- key 접근 -> 값 참조
- key 중복 불가

@author: wonseok
"""

person = {'name':'홍길동', 'age':35, 'addr':'서울시'}
print(person, len(person), type(person))

print(person['name']) # key -> value

# print(person[0]) # index 사용 불가

# 수정, 삭제, 추가, 검색: key를 사용
person['age'] = 40 # 수정
person

del person['addr']
person

person['pay'] = 250 # 추가
person

print('age' in person)

if 'age' in person:
    print('age 키 있음')
else:
    print('age 키 없음')


# 문자 빈도수 구하기 - 방법 1
charset = ['a', 'b', 'c', 'a', 'c', 'a'] # list
wc = {}

for ch in charset:
    if ch in wc: # wc에 ch가 있는 경우
        wc[ch] += 1
    else: # wc에 ch가 없는 경우
       wc[ch] = 1 # value 초기화

print(wc)

# 키 -> 값 참조
print(person)
person['name'] # '홍길동'
person.get('name') # '홍길동'
person.get('comm', 0) + 1


# 문자 빈도수 구하기 - 방법 2

wc2 = {}

for ch in charset:
    wc2[ch] = wc2.get(ch, 0) + 1 # 넘어오는 문자를 키로 지정 = get()으로 값 지정

print(wc2) # {'a': 3, 'b': 1, 'c': 2}

# for + dict

for key in person:
    print('key:', key, end = ' / ')
    print('value:', person[key])

for val in person.values():
    print(val)

for key, val in person.items():
    print(key, val)

for key_vals in person.items():
    # print(key_vals) # tuple : 순서 존재
    print('key:', key_vals[0], end = ' / ')
    print('values:', key_vals[1])


# {key: [value1, value2]}
emp = {'hong': [250, 50], 'lee': [350, 80], 'yoo': [200, 40]}
print(emp, len(emp))

# 급여가 250 이상인 사원명 출력하기
su_tot = 0
for k, v in emp.items():
    if v[0] >= 250:
        print(k)
        su_tot += v[1]

print('수당의 합계:', su_tot)

# 총 급여 = 급여 + 보너스
pay = {'hong': 200, 'lee': 300, 'kim': 210}
bonus = {'hong': 50, 'lee': 80, 'kim': 0}

# list + for
pays = [pay[k] + bonus[k] for k in pay]
print('각 사원의 급여:', pays)
print('총 급여:', sum(pays))
print('평균 급여:', sum(pays) / len(pays))

