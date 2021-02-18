'''
 문) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오. 
    조건> <tr> 태그 하위 태그인 <th> 태그의 모든 내용 출력
    
   <출력 결과>
   th 태그 내용 
    아이디 
    비밀번호 
'''

from bs4 import BeautifulSoup
import os # file path or dir 

os.chdir('C:/ITWILL/3_Python-I/workspace/chap08_Crawling/data')

# 1. 파일 읽기 
file = open("login.html", mode='r', encoding='utf-8')
source = file.read()

# 2. html 파싱
html = BeautifulSoup(source, 'html.parser')
print(html)

# 3. 태그 찾기 
ths = html.find_all('th')
print(len(ths)) # 2
print(ths)
'''
[<th> 아이디 </th>, <th> 비밀번호 </th>]
'''

# 4. 태그 내용 출력 
print('th 태그 내용')
for th in ths :
    print(th.string)
'''
th 태그 내용
 아이디 
 비밀번호
'''








