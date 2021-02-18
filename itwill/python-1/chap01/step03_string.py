# -*- coding: utf-8 -*-
"""
step03_string.py

1. 진법변환
2. 문자열(string) 처리 
3. escape 문자 
"""

# 1. 진법변환 : 10진수 <-> 2,8,16진수 
print(10, bin(10), oct(10), hex(10)) # 10진수 -> 2,8,16진수
# 10 0b1010 0o12 0xa

print(10, 0b1010, 0o12, 0xa) # 2,8,16진수 -> 10진수
# 10 10 10 10


# 2. 문자열(string) 처리
'''
 - 문자열 : 문자들의순서 있는 집합
 - 문자 분리 가능 : 순서 존재 
 - indexing/slicing 가능
 - 수정이 불가능  
'''

# 1) 문자열 유형 : 한 줄, 여러 줄 
lineStr = "this is one line string" # 한 줄 문자열 

multiStr = """this
is multi line
string"""  # 여러 줄 문자열 

multiStr2 = "this\n is multi line\n string" # 줄바꿈 : \n

print(lineStr) # this is one line string
print(multiStr)
'''
this
is multi line
string
'''
print(multiStr2)


# SQL문 : 부서번호 조회 
no = int(input('부서번호 입력 : '))
sql = f"""select * from emp
where deptno = {no}
order by sal desc"""

print(sql)
'''
select * from emp
where deptno = 20
order by sal desc
'''

# 2) 문자열 연산(+, *)
print('python' + ' ' + 'program') # + : 결합연산자 
# python program

# python3.8.exe
print('python' + str(3.8) + '.exe') # python3.8.exe

print('-'*50) # 문자열 반복 
print('*'*30)

# 3) indexing/slicing 가능
'''
R : index[1]
Python : index[0]
'''
lst = [1,2,3,4,5]
lst[1] # 2 
lst[0] # 1 -> 첫번째 원소 

print(lineStr) # this is one line string

# 왼쪽 기준 indexing 
len(lineStr) # 23
lineStr[0] # 't' - 첫번째 문자 
lineStr[0:4] # [시작:종료-1] : 1~4 문자열 : 'this'
lineStr[:4]

# 오른쪽 기준 index : -
lineStr[-1] # 맨마지막 문자 : 'g'
lineStr[-6:] # 끝에서 6개 문자 : 'string'
lineStr[-6:-1] # 'strin'

# slicing : 부분문자열 객체 
subStr = lineStr[-6:] # new object 
print(subStr) # string

print(id(subStr), id(lineStr)) # 1425840847280 1425841434672

if (subStr is lineStr) :
    print('동일 객체')
else :
    print('다른 객체') # 다른 객체 - False 


# 4) 문자열 처리 함수 
print(lineStr, type(lineStr)) # <class 'str'>
# this is one line string

# object.member

# (1) 문자 카운트 
print('t 글자수 :', lineStr.count('t')) # t 글자수 : 2

# (2) 접두어 판단 -> T/F
lineStr.startswith('this') # True
lineStr.startswith('that') # False

# (3) 문단 -> 문장 : split
print(multiStr)
'''
this
is multiline 
string
'''

sent = multiStr.split('\n') # 줄바꿈 
print(sent) # ['this', 'is multiline ', 'string']

# 문단 -> 단어 : split 
words = multiStr.split() # split(' ')
print(words) # ['this', 'is', 'multiline', 'string']
print('단어 길이 :', len(words)) # 단어 길이 : 4

'''
형태소 분석 : 문장 성분 분석(명사, 수사, 조사, 부사 등)
'''

# (4) 문자열 결합(join) : '구분자'.join(단어)
lines = ' '.join(words)
print(lines) # this is multiline string


# 3. escape 문자
'''
escape 문자 : 특수기능의 문자(\n, \t, \b, \r, '', "") -> 제어문자, 문자열 
'''
print('test')
print('\nescape 문자') # 적용 예
print('\\nescape 문자') # 기능 차단 : 방법1
print(r'\nescape 문자') # 기능 차단 : 방법2

# 경로표현 : c:\python\test
print('c:\python\test') # c:\python	est
print('c:\\python\\test') # c:\python\test
print('c:/python/test') # c:/python/test
print(r'c:\python\test') # c:\python\test

# 문) c:\'aa'\abc.txt 출력하기 
print("c:\\\'aa\'\\abc.txt") # 방법1
print(r"c:\'aa'\abc.txt") # 방법2












