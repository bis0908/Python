# -*- coding: utf-8 -*-
"""
step02_tag_name.py

1. tag 계층구조 찾기
2. find('tag')함수 찾기
"""

from bs4 import BeautifulSoup # 클래스 : html 파싱
import os # file path or dir

#os.chdir('C:/ITWILL/3_Python-I/workspace/chap08_Crawling/data')

# 1. 로컬 서버 파일 읽기
file = open('html01.html', mode='r', encoding='utf-8')
src = file.read()
print(type(src))  # <class 'str'>

# 2. html 파싱 : 소스 -> html문서 변환
html = BeautifulSoup(src, 'html.parser')
print(html)
print(type(html)) # <class 'bs4.BeautifulSoup'>


# 3. tag 내용 가져오기

# 1) tag 계층구조 찾기
h1 = html.html.body.h1 # <h1> 시멘틱 태그 ?</h1>
print('h1 :', h1.string) # h1 :  시멘틱 태그 ?

# 2) find('tag')함수 찾기
h2 = html.find('h2') # string
print('h2 :', h2.string) # h2 :  주요 시멘틱 태그

# 3) find_all('tag')함수 찾기
lis = html.find_all('li') # list
print(lis)
print(type(lis))
len(lis) # 5


for li in lis :
    print(li.string)

'''
 header : 문서의 머리말(사이트 소개, 제목, 로그 )
 nav : 네이게이션(메뉴)
 section : 웹 문서를 장(chapter)으로 볼 때 절을 구분하는 태그
 aside : 문서의 보조 내용(광고, 즐겨찾기, 링크)
 footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호)
'''

# 내용 변수 저장 : list + for
li_str = [li.string  for li in lis ]
print(li_str)
'''
[' header : 문서의 머리말(사이트 소개, 제목, 로그 )', ' nav : 네이게이션(메뉴) ', ' section : 웹 문서를 장(chapter)으로 볼 때 절을 구분하는 태그', ' aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) ', ' footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) ']
'''














