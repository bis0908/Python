# -*- coding: utf-8 -*-
"""
정규 표현식
 
[주요 메타문자]
. : 임의의 한 문자 
.x : 임의의 한 문자 뒤에 x가 오는 문자열(ex : abc, mbc -> .bc) 
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.) 
x* : x가 0번 이상 반복
x+ : x가 1개 이상 반복
x? : x가 0 또는 1개 존재
x{m, n} : x가 m~n 사이 연속 
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치   
"""

st1 = '1234 abc홍길동 ABC_555_6 이사도시'
st2 = 'test1abcABC 123mbc 45test'
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

# 방법1)
import re # 정규표현식 모듈 : 텍스트 처리 함수 제공 

# 방법2) 
from re import findall, match, sub 
#from 모듈 import 함수1, 함수2, 함수3, ...

'''
re.findall(pattern, string) # 방법1)
findall(pattern, string) # 방법2)
'''

# 1. findall(pattern, string) -> list 반환 

# 1) 숫자 찾기 
print(st1) # 1234 abc홍길동 ABC_555_6 이사도시
re.findall('1234', st1) # ['1234']
findall('[0-9]', st1) # ['1', '2', '3', '4', '5', '5', '5', '6']
findall('[0-9]{3}', st1) # ['123', '555']
findall('[0-9]{3,4}', st1) # ['1234', '555']
findall('\\d{3}', st1) # '[0-9]{3}' - ['123', '555']

# 2) 문자열 찾기 
findall('[가-힣]{3,}', st1) # ['홍길동', '이사도시']
findall('[a-z]{3}', st1) # ['abc']
findall('[a-z|A-Z]{3}', st1) # ['abc', 'ABC']

type(st1) # str

st_split = st1.split() # 공백 기준 -> 토큰 생성 
print(st_split) # ['1234', 'abc홍길동', 'ABC_555_6', '이사도시']

names = [] # 이름 저장 
for st in st_split : # '1234' > 'abc홍길동'
    name = findall('[가-힣]{3,}', st) # [] > ['홍길동']
    
    if name : # name=[] -> False
        #names.append(name) # 중첩 list
        names.extend(name) # 단일 list
        
print('names :', names)        
'''
append()
names : [['홍길동'], ['이사도시']] -> 2차원([2x1]) 
names : ['홍길동', '이사도시'] -> 1차원([2]) 
'''    

# 3) 접두어/접미어 추출 
st2 = 'test1abcABC 123mbc 45test'

findall('^test', st2) # ['test'] - 접두어 
findall('test$', st2) # ['test'] - 접미어 
findall('mbc$', st2) # []


# 종료/시작 문자 찾기
findall('.bc', st2) # ['abc', 'mbc']
findall('t.', st2) # ['te', 't1', 'te']


# 4) 단어 찾기(\\w) : 한글,영문,숫자 
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

words = findall('\\w{3,}', st3) # 3음절 이상 단어 추출 
print(words) # ['test', '홍길동', 'abc', '123', 'tbc']


# 5) 문자열 제외 : [^x]
re = findall('[^t]+', st3) # + : 1개 이상 반복 
print(re, len(re)) # ['es', '^홍길동 abc 대한*민국 123$', 'bc'] 3

# 불용어(특수문자) 제거 
findall('[^^*$]+', st3) #  ['test', '홍길동 abc 대한', '민국 123', 'tbc']

# exam01 


# 2. match(pattern, string) : object(Yes) or NULL(No)
# - 패턴 일치 여부 반환 

jumin = '123456-1234567'
re = match('[0-9]{6}-[1-4][0-9]{6}', jumin)

print(re) # None -> False

if re :
    print('올바른 주민번호') # 올바른 주민번호
else :
    print('잘못된 주민번호')


# 3. sub(pattern, repl, string)

st3 = 'test^홍길동 abc 대한*민국 123$tbc'

text = sub('[\^*$]', '', st3)
print('text :', text) # text : test홍길동 abc 대한민국 123tbc


# exam02 ~ 03














