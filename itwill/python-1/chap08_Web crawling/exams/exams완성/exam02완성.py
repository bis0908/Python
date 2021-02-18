'''
 문2) urls 객체의 url을 대상으로 다음 조건에 맞게 웹 문서의 자료를 수집하시오.
    조건1> http://으로 시작하는 url만을 대상으로 한다.
    조건2> url에 해당하는 웹 문서를 대상으로 <a> 태그 내용만 출력한다.
    조건3> <a> 태그 내용이 없는(None) 경우는 출력하지 않는다.

    <출력 결과 예시>
    a tag 내용 :  OTTOGI
    a tag 내용 :  NONGSHIM
       중간 생략
    a tag 내용 :  네이버 정책
    a tag 내용 :  고객센터
    a tag 내용 :  ⓒ NAVER Corp.
'''

from urllib.request import urlopen # 함수 : 원격 서버 url 요청 
from bs4 import BeautifulSoup # 클래스 : html 파싱
import re # 정규표현식

urls = ['http://www.daum.net', 'www.daum.net', 'http://www.naver.com']

# 단계1 : url 정제
new_urls = []
for url in urls :
    tmp = re.findall('^http://', url)
    if tmp :
        new_urls.append(url)

# 단계2 : url에서 a 태그 내용 수집 & 출력
for url in new_urls :   
    # 1. url 요청
    print('url :', url)
    req = urlopen(url)
    data = req.read()
    
    # 2. html 파싱 
    src = data.decode('utf-8')
    html = BeautifulSoup(src, 'html.parser')
    
    # 3. a 태그 찾기 & 내용 
    a_all = html.find_all('a') # 앵커 태그 전체 찾기 
    print('a 태그 전체 개수 :', len(a_all)) # a 태그 전체 개수 : 414
    
    for a in a_all : 
        
        if a.string : # None == False
            print(a.string) # tag 내용 출력
            
    
    
    
    
    
    
    
    
    
    
    
    
    

