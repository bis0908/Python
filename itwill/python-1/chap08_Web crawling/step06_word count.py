# -*- coding: utf-8 -*-
"""
step06_word count

news > 전처리 > 단어 빈도 수 > 시각화

@author: wonseok
"""

import pickle
import os

os.chdir('E:\Code\Python\itwill\chap08_Web crawling\data')

# pickle filw load
file = open('news_data.pickle', mode = 'rb')
news_data = pickle.load(file)
file.close()

# text 전처리

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
    spec_st = '[@#$%^&*\()]'
    texts_re4 = [sub(spec_st, '', t) for t in texts_re3]

    # 단계5 : 공백제거 : 2칸 이상 공백 -> 1칸 공백
    texts_re5 = [ ' '.join(t.split())  for t in texts_re4]

    return texts_re5


news_clean_data = clean_texts(news_data)

# 단어 빈도 수: 공백 기준 단어 생성
word_count = {}
for texts in news_clean_data:
    for word in texts.split():
        word_count[word] = word_count.get(word, 0) + 1

# word_count = [word_count for texts in news_clean_data for word in texts.split()]

# copy
word_count2 = word_count.copy()

for word in word_count.keys():  # word search
    if len(word) < 2:
        del word_count2[word]   # delect word


# top 5 word
from collections import Counter
counter = Counter(word_count2)
del counter['[바로잡습니다]']

top10_word = counter.most_common(10)

words = []
cnt = []

for word in top10_word:
    words.append(word[0])
    cnt.append(word[1])

import matplotlib.pyplot as plt
# 차트에 한글 지원
plt.rcParams['font.family'] = 'D2coding'

# bar chart
plt.bar(words, cnt)
plt.title('뉴스 단어 출현 빈도 수 분석')
plt.show()

# line graph
plt.plot(words, cnt)
