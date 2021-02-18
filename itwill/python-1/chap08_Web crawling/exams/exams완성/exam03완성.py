'''
 문3) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오.
    조건1> id="login_wrap" 선택자의  하위 태그  전체 출력 
    조건2> id="login_warp" 선택자 > form > table 태그 내용 출력 
    조건3> find_all('tr') 함수 이용  th 태그 내용 출력 
'''

from bs4 import BeautifulSoup 
import os # file path or dir 

os.chdir('C:/ITWILL/3_Python-I/workspace/chap08_Crawling/data')


# html source 가져오기 
file = open('login.html', mode='r', encoding='utf-8')
html = file.read()

# html 파싱
html = BeautifulSoup(html, 'html.parser')

# 3. 선택자 이용 태그 내용 가져오기 

# 1) id 선택자 : <div id="login_wrap">
print('1. id 선택자')
div = html.select_one("div#login_wrap")
print(div) # table 전체 내용 출력 

# 2) id 선택자 > form 태그 > table 태그  출력
print('2. id 선택자 > from > table') 
table = html.select_one("#login_wrap > form > table") # 계층적으로 접근 : 열 제목
print(table) 

# 3) tr > th/td 태그 내용 출력
print('3. tr > th 태그 내용 출력') 
trs = html.find_all("tr")
print(trs) # [<tr> </tr>, <tr> </tr>]

print('\nth 내용')
for tr in trs : 
    th = tr.find('th') # 요소 추출 
    print(th.string) # 내용 추출 
'''
<th> 아이디 </th>
<th> 비밀번호 </th>
 아이디 
 비밀번호
'''
