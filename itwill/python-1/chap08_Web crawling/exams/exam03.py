'''
 문3) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오.
    조건1> id="login_wrap" 선택자의  하위 태그  전체 출력
    조건2> id="login_wrap" 선택자  > form > table 태그 내용 출력
    조건3> find_all('tr') 함수 이용  th 태그 내용 출력
'''

from bs4 import BeautifulSoup

# 1. html source 가져오기
file = open('login.html', mode = 'r', encoding = 'utf-8')


# 2. html 파싱
src = file.read()
print(src)
file.close()

html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. 선택자 이용 태그 내용 가져오기
# 3.1
table = html.select_one('#login_wrap') # <table border="1" id="tab"> ~ 모든 내용 </table>
print(table)

# 3.2
tab = table.select('form > table')
print(tab)

# 3.3
trs = html.find_all('tr')

for tr in trs:
    th = tr.find('th')
    print(th.string)


