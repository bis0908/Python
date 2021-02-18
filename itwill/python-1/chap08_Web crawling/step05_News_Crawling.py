# -*- coding: utf-8 -*-
"""
step05_News_Crawling

1. news crawling
    url: http://media.daum.net

2. pickle file save
    news 자료: 이진파일 저장

@author: wonseok
"""
# import requests
from urllib.request import urlopen # 함수 : 원격 서버 url 요청
from bs4 import BeautifulSoup # 클래스 : html 파싱
import os
import pickle

os.chdir('E:\Code\Python\itwill\chap08_Web crawling\data')

# url 요청 -> 응답
url = 'http://media.daum.net'
req = urlopen(url)
data = req.read()

src = data.decode('utf-8')
html = BeautifulSoup(src, 'html.parser')

links = html.select("a[class = 'link_txt']")
print(len(links))

news_data = []
    for link in links:
        tmp = str(link.string)
        if tmp != 'None':
            news_data.append(tmp.strip())

print(news_data)
print(len(news_data))
print(type(news_data))

# 2. save to pickle file
# save: pickle.dump(obj, file)
# load: pickle.load(fike)

# save
file = open('news_data.pickle', mode = 'wb')
pickle.dump(news_data, file)
print('file saved by pickle')

# load
file = open('news_data.pickle', mode = 'rb')
news_data2 = pickle.load(file)
print(news_data2)
file.close()