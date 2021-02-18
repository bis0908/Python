# -*- coding: utf-8 -*-
"""
step04_set

set 특징
- 비 순서 자료구조(index 사용 불가)
- 중복 허용 불가
형식) 변수 = set(value) or set([value]) or {value}

@author: wonseok
"""

s = set([1, 2, 3, 4]) # == {1, 2, 3, 4}
print(s, len(s), type(s))

# for + set
for i in s:
    print(i, end = ' ')

# 중복 불가
gender = ['남', '여', '남', '여']
set([gender]) # TypeError: unhashable type: 'list'

# list -> set
sgender = set(gender)
print(sgender)

print(sgender[0]) # TypeError: 'set' object is not subscriptable

# set -> list
gender = list(sgender)
print(gender[0])

# set Member
s2 = {3, 6}
s3 = {1, 3, 5}

s2.add(5) # 원소 추가
print(s2) # {3, 5, 6}

# 집합 관련
s2.union(s3) # {1, 3, 5, 6}
s2.difference(s3) # {6} -> 차집합
s2.intersection(s3) # {3, 5} -> 교집합

# 원소 삭제
s3.discard(3) # 없는데 삭제 시도시 에러 발생하지 않는다.
s3.remove(5) # 에러가 발생함.


