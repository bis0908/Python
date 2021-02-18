# -*- coding: utf-8 -*-
"""
step06_Module

패키지: 폴더; 관련 모듈을 꾸러미 제공
모듈: 파일; 클래스와 함수로 구성된 파이썬 파일

@author: wonseok
"""

# 사전 수행 내용: 패키지 폴더에 참조 파일이 있어야 한다.

import os

os.getcwd() # 'E:\\Code\\Python\\itwill\\Package'
os.chdir('E:\Code\Python\itwill')

# 방법 1
from Package.module01 import adder, sub

x = 10; y = 20
print('adder = ', adder(x, y))

obj = sub(x, y) # 생성자 -> object
obj.calc()

# 방법 2 - 코드가 길어진다
import Package.module01

Package.module01.addr(x, y)
obj1 = Package.module01.sub(x, y)
obj1.calc()

