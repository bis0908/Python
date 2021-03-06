# -*- coding: utf-8 -*-
"""
step05_newsCrawling.py

1. news Crawling
   url : http://media.daum.net
2. pickle file save
   news 자료 : 이진파일(binary file) 저장 
"""

from urllib.request import urlopen # 함수 : 원격 서버 url 요청 
from bs4 import BeautifulSoup # 클래스 : html 파싱
import os # file save

# file 저장 위치 
os.chdir('C:/ITWILL/3_Python-I/workspace/chap08_Crawling/data')

########################
# 1. news Crawling
########################

# 1.url 요청 -> 응답 
url = 'http://media.daum.net'

req = urlopen(url)
data = req.read() # source 
print(data)

# 2. html 파싱 
src = data.decode('utf-8')
html = BeautifulSoup(src, "html.parser")
print(html)

# 3. tag 찾기 -> 내용 수집 
# 형식) select('태그[속성='값']')
# 1) tag 수집 
links = html.select("a[class='link_txt']")
print(len(links)) # 62

print(links[0])
print(links[-1])

# 2) tag 내용 가져오기 
news_data = [] # news 저장 
for link in links :
    tmp = str(link.string) # 기사 내용 
    if tmp != 'None' : # not None
        news_data.append(tmp.strip()) # 문장 끝 불용어 제거
    
print(news_data)
print(len(news_data)) # 43
print(type(news_data)) # <class 'list'>
    
########################
# 2. pickle file save
########################
import pickle

'''
pickle 
 - list, dict 객체를 binary 형태로 저장 
 
save : pickle.dump(obj, file)
load : pickle.load(file) 
'''

# save 
file = open('news_data.pickle', mode='wb')
pickle.dump(news_data, file)
print('pickle file saved...')
file.close()


# load 
file = open('news_data.pickle', mode='rb')
news_data2 = pickle.load(file)
print(news_data2)
file.close()











