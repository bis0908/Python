# -*- coding: utf-8 -*-
"""
변수(variable)
 - 형식) 변수명 = 값 or 수식 or 변수명 
 - 자료(객체:object)가 저장된 메모리 주소 저장 이름 
 - 참조변수(R 동일함) 
 - type 선언 없음(R 동일함)
"""

# 1. 변수와 자료형 
var1 = 'Hello Python'
var2 = "Hello Python"

# 콘솔출력 : print() - 줄바꿈 포함 
print(var1) # Hello Python
print(var2) # Hello Python

# 자료형 : type()
print(type(var1)) # <class 'str'>
print(type(var2)) # <class 'str'> -> 문자형 

var1 = 100 # 수정 
print(var1, type(var1)) # 100 <class 'int'> -> 정수형 

var3 = 150.1235
print(var3, type(var3)) # 150.1235 <class 'float'> -> 실수형 

var4 = True # keyword
print(var4, type(var4)) # True <class 'bool'> -> 논리형 


# 2. 변수명 작성 규칙(ppt.12)
'''
- 첫자 : 영문자 or _
- 대소문자 구분 : Score, score
- 낙타체 : 두 이상 단어 결합(korScore)
- 키워드 또는 기존 함수명 사용불가, 한글 비권장 
'''

_num10 = 10
_Num10 = 10.012

print(_num10 * 2) # 20
print(_Num10 * 2) # 20.024

# 명령어 확인 
import keyword # 모듈 가져오기 

py_kw = keyword.kwlist # 모듈.멤버 -> 멤버 호출
print(py_kw) # vector 변수   
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

# 원소 길이 : len()
print('키워드 개수 =', len(py_kw)) # 키워드 개수 = 35












