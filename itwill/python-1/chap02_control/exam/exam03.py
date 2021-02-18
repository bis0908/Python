'''
step03 관련 문제

문) word count
   - 여러 줄의 문자열에서 공백을 기준으로 단어를 분류하고, 단어 수 출력하기
'''

multiline="""안녕 Python 세계로 오신걸
환영 합니다.
파이션은 비단뱀 처럼 매력적인 언어 입니다."""


# <<출력 결과>>
'''
안녕
Python
세계로
오신걸
환영
합니다.
파이션은
비단뱀
처럼
매력적인
언어
입니다.
단어수 : 12
'''

leng = multiline.split()

for i in range(len(leng)):
    print(leng[i])
    if i == 11:
        print('단어수: {}'.format(len(leng)))


for i in 0:len(leng):
    print(leng[i])
    if i == 11:
        print('단어수: {}'.format(len(leng)))
