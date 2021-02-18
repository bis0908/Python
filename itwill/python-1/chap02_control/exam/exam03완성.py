'''
step03 관련 문제

문) word count
   - 여러 줄의 문자열에서 공백을 기준으로 단어를 분류하고, 단어 수 출력하기
'''

multiline="""안녕 Python 세계로 오신걸
환영 합니다.
파이션은 비단뱀 처럼 매력적인 언어 입니다."""


# 공백 문자를 기준으로 단어수 카운터
doc = [] # 빈 list : 줄 단위 저장
words  = [] # 빈 list : 단어 저장
    
for line in multiline.split("\n"):   
    doc.append(line) # 줄 단위 문장을 빈 list에 추가    
    for w in line.split(" "): # 공백으로 분리
        words.append(w)
        print(w)
print('단어수 :',len(words)) # 단어수 출력

'''
안녕하세요.
Python
세계로
오신걸
환영합니다.
파이션은
비단뱀
처럼
매력적인
언어입니다.
단어수 : 10
'''