# -*- coding: utf-8 -*-
"""
step02_newsQueryCrawling.py

url query 형식 
http://url?변수=값&변수=값 

1. url : http://media.daum.net -> 배열 이력 
2. https://news.daum.net/newsbox  -> 특정 날짜 선택 
3. https://news.daum.net/newsbox?regDate=20210201 -> 특정 page 선택 
4. https://news.daum.net/newsbox?regDate=20210201&tab_cate=NE&page=2
4. https://news.daum.net/newsbox?regDate=20210201&tab_cate=NE&page=3

[실습내용]
1. 날짜 : 20210201 ~ 20210228
2. page : 1~10page
28 * 10 = 280 page 
"""

from urllib.request import urlopen # 함수 : 원격 서버 url 요청 
from bs4 import BeautifulSoup # 클래스 : html 파싱


# 1. url query 만들기 
base_url = "https://news.daum.net/newsbox?regDate="
date = list(range(20210201, 20210229)) # 20210201~20210228
date
len(date) #  28

# regDate
url_list = [base_url + str(d) for d in date]
url_list
# https://news.daum.net/newsbox?regDate=20210228

# page : &page= 1 ~ &page= 10
pages = ['&page=' + str(p) for p in range(1, 11)]
pages

# url(1) vs pages(10)
final_url = [] # 280개 

for url in url_list : # 28
    for page in pages : # 10
        # 28 * 10 = 280
        final_url.append(url+page)

len(final_url) # 280
final_url[0] # 첫번째 url
# 'https://news.daum.net/newsbox?regDate=20210201&page=1'
final_url[-1] # 마지막 url 
# 'https://news.daum.net/newsbox?regDate=20210228&page=10'


# 2. Crawling function : Crawler
def Crawler(url) :
    # 1. url 요청 
    req = urlopen(url)
    data = req.read() # source 
    
    # 2. html 파싱 
    src = data.decode('utf-8')
    html = BeautifulSoup(src, "html.parser")
    
    links = html.select('a[class=link_txt]') # element 수집 
    #print(links) # tag + news
    
    one_page_news = [] # 1 page 뉴스 
    
    for link in links :
        cont = str(link.string).strip()
        one_page_news.append(cont)
        
    return one_page_news    
    
        
one_page_news = Crawler(final_url[0])    

len(one_page_news) # 134
   
one_page_news[39]

one_page_news[40] # 많이본 뉴스 ~ 

# 해당 page에서 유효한 news
one_page_news[:40]


# 2월 전체 news 
month_news = []
page_cnt = 0 

# 3. Crawler 호출 
for url in final_url :
    page_cnt += 1
    print('page 번호 :', page_cnt)
    print('url : ', url)
    
    try : # 예외처리 : url 없는 경우 
        one_page_news = Crawler(url) # 1page news 
        month_news.extend(one_page_news[:40])  # 단일 list 
    except :
        print('해당 url 없음 : ', url)
print(month_news)

len(month_news) # 11200
28 * 10 * 40 # 11200

type(month_news) #  list


# 4. file save
import pickle 

path = "C:/ITWILL/4_Python-II/workspace/chap07_Text_Mining/"

file = open(path + 'news_data.pickle', mode='wb') 
pickle.dump(month_news, file)
file.close()

file = open(path + 'news_data.pickle', mode='rb')
news_data = pickle.load(file)

print(news_data)
file.close()












