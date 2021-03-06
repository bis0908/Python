# -*- coding: utf-8 -*-
"""
step02_news_Query_Crawling

url query 형식
http://url?query (변수 = 값)

1. url = 'http://media.daum.net'
2. https://news.daum.net/newsbox
3. https://news.daum.net/newsbox?tab_cate=NE&regDate=20210301
4. https://news.daum.net/newsbox?regDate=20210201&tab_cate=NE&page=2
@author: wonseok
"""

from urllib.request import urlopen # 함수 : 원격 서버 url 요청
from bs4 import BeautifulSoup # 클래스 : html 파싱

# 1. url query 만들기
base_url = 'https://news.daum.net/newsbox?regDate='
date = list(range(20210201, 20210229))
date
len(date) # 28

# regDate
url_list = [base_url + str(d) for d in date]
url_list

# page: &page=1 ~ 10
pages = ['&page=' + str(p) for p in range(1, 11)]
pages

# url(1) vs pages(10)
final_url = [] # 280개

for url in url_list:
    for page in pages:
        final_url.append(url+page)

final_url


# 2. Crawling function
def Crawler(url):
    # request url
    req = urlopen(url)
    data = req.read()

    # parsing
    src = data.decode('utf-8')
    html = BeautifulSoup(src, 'html.parser')

    links = html.select('a[class = "link_txt"]')
    # print(links)

    one_page_news = []

    for link in links:
        cont = str(link.string).strip()
        one_page_news.append(cont)

    return one_page_news

one_page_news = Crawler(final_url[0])

one_page_news

# 2월 전체 news
