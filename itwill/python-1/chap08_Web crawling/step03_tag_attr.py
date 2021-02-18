# -*- coding: utf-8 -*-
"""
step03_tag_attr.py

tab 속성과 내용 가져오기

element : tag + 속성 + 내용
 <a href="www.naver.com"> 네이버 </a>
 -> a : tag
 -> href : 속성(attribute)
 -> 네이버 : 내용(content)
"""

from bs4 import BeautifulSoup # html 파싱
import os # file path

os.chdir('E:\Code\Python\itwill\chap08_Web crawling\data')

# 1. 로컬 서버 파일 읽기
file = open('html02.html', mode = 'r', encoding = 'utf-8')
src = file.read()
print(type(src))  # <class 'str'>
file.close()

# 2. html 파싱 : 소스 -> html문서 변환
html = BeautifulSoup(src, 'html.parser')
print(html)
print(type(html)) # <class 'bs4.BeautifulSoup'>


# 3. 태그 속성과 내용 가져오기
links = html.find_all('a')
print(links)

urls = [] # url 저장
for link in links :
    print(link.string) # obj.string : 내용
    print(link.attrs) # obj.attrs : 속성
    # {'href': 'www.naver.com'} - dict{'속성':'값'}

    # 예외처리
    try :
        url = link.attrs['href']
        urls.append(url)
        print(link.attrs['target']) # KeyError: 'target'
    except Exception as e :
        print('예외발생 :', e)


print(urls)
# ['www.naver.com', 'http://www.naver.com', 'http://www.naver.com', 'www.duam.net', 'http://www.duam.net']


# 4. 정규표현식으로 속성 선택하기
# - 정상 url 필터링
import re

new_urls = [] # 정상 url
for link in links :
    url = link.attrs['href']

    # str 객체의 메서드
    if url.startswith('http://') :
        print(url)

    # 정규표현식
    tmp = re.findall('^http://', url)

    if tmp : # [] -> false
        new_urls.append(url)

print(new_urls)
# ['http://www.naver.com', 'http://www.naver.com', 'http://www.duam.net']


# exam02.py












