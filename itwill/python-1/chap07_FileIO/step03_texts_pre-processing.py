# -*- coding: utf-8 -*-
"""
step03_texts_pre-processing

@author: wonseok
"""

import os

os.chdir('E:\Code\Python\itwill\chap07_FileIO\data')

os.getcwd()

def clean_texts(texts) :
    from re import sub #form 모듈 import 함수

    # 단계1 : 소문자 변경
    texts_re = [t.lower() for t in texts ]

    # 단계2 : 숫자 제거
    texts_re2 = [sub('[0-9]', '', t) for t in texts_re]

    # 단계3 : 문장부호 제거
    punc_st = '[,.;:?!]'
    texts_re3 = [sub(punc_st, '', t) for t in texts_re2]

    # 단계4 : 특수문자 제거
    spec_st = '[@#$%^&*()]'
    texts_re4 = [sub(spec_st, '', t) for t in texts_re3]

    # 단계5 : 공백제거 : '구분자'.join(word)
    texts_re5 = [' '.join(t.split())  for t in texts_re4]

    return texts_re5

try:
    # file read / 전처리
    rfile = open('texts.txt', encoding = 'utf-8')

    texts = rfile.readlines()
    print(texts)

    texts_re = [row.strip() for row in texts]
    texts_re = clean_texts(texts)

    print('**after text pre-processing**')
    print(texts_re)
    print('문장 길이: ', len(texts))
    '''
    # file save; 새 파일을 만들고 열어서 거기에 데이터 적재 시키기
    wfile = open('texts_write.txt', mode = 'w', encoding = 'utf-8')
    for texts in texts_re:
        wfile.write(texts + '\n')

    print('text file saved...')
    '''
    # word count
    words = []
    wc = {}
    rfile2 = open('texts_write.txt', mode = 'r', encoding = 'utf-8')

    texts = rfile2.readlines()

    # word 추출
    for row in texts:
        for word in row.split():
            words.append(word)

    print('words : ', words, len(words))

    for word in words:
        wc[word] = wc.get(word, 0) + 1

    print(wc) # dict

    # 출현 빈도 높은 단어
    print('max = ', max(wc, key = wc.get))
    # 출현빈도수 기준 단어 내림정렬
    wc_sorted = sorted(wc, key = wc.get, reverse = True)
    print(wc_sorted)

    print('Top 5 word is : ', wc_sorted[:5])

    # top 5 vs 출현 빈도
    for word in wc_sorted:
        print(word, wc[word], sep = ' -> ') # value


except Exception as e:
    print('Err code: ', e)

finally:

    # wfile.close();
    rfile.close(); rfile2.close()

