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

import urllib.request as req # 원격 서버 파일 요청
from bs4 import BeautifulSoup # html 파싱
import re # 정규표현식

urls = ['http://www.daum.net', 'www.daum.net', 'http://www.naver.com']

# 단계1 : url 정제
new_urls = []

# 단계2 : url에서 a 태그 내용 수집 & 출력
