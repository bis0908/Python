# -*- coding: utf-8 -*-
"""
문제3) obama.txt(오바바 연설문) 파일을 읽어와서 텍스트를 전처리한 후 다음과 같이 출력하시오.

  <출력 예시>
전체 단어수 = 4,907개
최고 출현 단어 :  the
top10 word = ['the', 'and', 'of', 'to', 'our', 'that', 'a', 'you', 'we', 'applause']

단어 빈도수
the : 205
and : 195
of : 152
to : 140
our : 109
that : 91
a : 83
you : 82
we : 81
applause : 75
"""
import os


# 텍스트 전처리 함수
def clean_texts(texts) : # texts = 문단(문장들)
    from re import sub #form 모듈 import 함수

    # 단계1 : 소문자 변경
    texts_re = [t.lower() for t in texts ]

    # 단계2 : 숫자 제거
    texts_re2 = [sub('[0-9]', '', t) for t in texts_re]

    # 단계3 : 문장부호 제거
    punc_st = '[,.;:?!]'
    texts_re3 = [sub(punc_st, '', t) for t in texts_re2]

    # 단계4 : 특수문자 제거
    spec_st = '[@#-$%^&*()\n]'
    texts_re4 = [sub(spec_st, '', t) for t in texts_re3]

    # 단계5 : 공백제거 : 2칸 이상 공백 -> 1칸 공백
    texts_re5 = [ ' '.join(t.split())  for t in texts_re4]

    return texts_re5


try :
    # 1.파일 읽기(절대경로)
    os.chdir('E:\Code\Python\itwill\chap07_FileIO\data')
    rfile = open('obama.txt', mode = 'r') # / or \\
    #print(rfile.read()) # 파일 전체 읽기

    texts = rfile.readlines()
    print(texts)
    #texts_re = ''.join(texts)
    #texts_re = [row.strip() for row in texts]
    texts_re = [row.strip() for row in texts]
    texts_re = clean_texts(texts_re)


    # 2.줄 단위 텍스트 전처리
    words = []
    wc = {}

    '''
    for row in texts_re1:
        for word in row.split():
            words.append(word)
    '''
    # 이중 for 문을 한 줄로 -> http://asq.kr/xSKzcUylgijQ6i
    words = [word for row in texts_re for word in row.split()]
    len(texts_re)
    len(words)

    # 3. word count
    for word in words:
        # Dict.get(): 특정 키에 대한 값을 리턴 -> '.get(key, default)'
        wc[word] = wc.get(word, 0) + 1
    len(wc)
    print('Total word count:', len(words))
    print('Max counted word is :', max(wc, key = wc.get))

    wc_sorted = sorted(wc, key = wc.get, reverse = True)

    print('Top 10 word is :', wc_sorted[:10])

    print('*' * 30)
    for word in wc_sorted[:10]: # 빈도수 상위 10개만

        print(word, wc[word], sep = ' -> ') # value
    print('*' * 30)

except Exception as e:
    print('!!! Error 발생 :', e)
finally:
    rfile.close()
    #wfile.close()



