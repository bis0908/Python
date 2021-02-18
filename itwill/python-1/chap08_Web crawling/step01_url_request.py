# -*- coding: utf-8 -*-
"""
step01_url_request.py

<작업 절차>
1. url 요청 -> 응답
2. source -> html 파싱(html 문서 변환)
3. 태그(tag) 검색 -> 내용 가져오기
   <a href='www.duam.net'> 다음 카카오 </a>
   <img src='a.png'/>
"""
from urllib.request import urlopen # 함수 : 원격 서버 url 요청
from bs4 import BeautifulSoup # 클래스 : html 파싱
'''
pip install beautifulsoup4
'''
url = "http://www.naver.com/index.html"

# 1. 원격 서버 url 요청
req = urlopen(url) # 응답
data = req.read() # source 읽기
print(data)

# 2. html 파싱 : source -> html 문서 변환
src = data.decode('utf-8') # charset="utf-8"
html = BeautifulSoup(src, 'html.parser')
print(html) # html 문서

# 3. 태그 내용 가져오기
a_all = html.find_all('a') # 앵커 태그 전체 찾기
print('a 태그 전체 개수 :', len(a_all)) # a 태그 전체 개수 : 414

print(a_all) # list

a_first = a_all[0]
print(a_first)
# <a href="#newsstand"><span>뉴스스탠드 바로가기</span></a>

print('a 태그 내용 :', a_first.string)
# a 태그 내용 : 뉴스스탠드 바로가기