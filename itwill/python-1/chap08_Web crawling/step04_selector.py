# -*- coding: utf-8 -*-
"""
step04_selector

선택자(selector) 이용 자료 수집
 - 웹문서 디자인용으로 사용
 - 선택자: id, class
 - id: 중복 불가 -> 1개 tag 선택
 - class: 중복 가능 -> n개 tag 선택

 html.select_one(#id)
 html.select(.class)

@author: wonseok
"""

from bs4 import BeautifulSoup # html 파싱
import os # file path

os.chdir('E:\Code\Python\itwill\chap08_Web crawling\data')

# 1. 로컬 서버 파일 읽기
file = open('html03.html', mode = 'r', encoding = 'utf-8')
src = file.read()
print(type(src))  # <class 'str'>
file.close()

# 2. html 파싱 : 소스 -> html문서 변환
html = BeautifulSoup(src, 'html.parser')
print(html)
print(type(html)) # <class 'bs4.BeautifulSoup'>


# 3.    selector
# 3.1   id 수집
table = html.select_one('#tab') # <table border="1" id="tab"> ~ 모든 내용 </table>
print(table)

tds = table.find_all('td')

for td in tds:
    print(td.string)

# 선택자 & 계층구조
ths = html.select('#tab > tr > th')

for th in ths:
    print(th.string)


# 3.2   class 선택자: .class id
trs = html.select('#tab > .odd')

# td 태그의 내용 출력하기
for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        print(td.string)

# 3.3   select("tag[attr = 'value']")
trs = html.select("tr[class = 'odd']")
print(trs)


