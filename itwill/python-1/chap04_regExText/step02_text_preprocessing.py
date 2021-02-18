# -*- coding: utf-8 -*-
"""
re 모듈 이용 -> 텍스트 전처리 
"""

from re import sub #form 모듈 import 함수  

# 텍스트 전처리 : file
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']

# 단계1 : 소문자 변경
'''
texts_re = [] # 전처리 결과 save
for t in texts : # 'AFAB54747,asabag?'
    texts_re.append(t.lower()) # 소문자 변경 -> 추가 
'''    
# list + for 
texts_re = [t.lower() for t in texts ]   
print(texts_re) # ['afab54747,asabag?', 'abtta $$;a12:2424.', 'uysfsfa,a124&***$?']   


# 단계2 : 숫자 제거 
texts_re2 = [sub('[0-9]', '', t) for t in texts_re]
print(texts_re2) # ['afab,asabag?', 'abtta $$;a:.', 'uysfsfa,a&***$?']


# 단계3 : 문장부호 제거 
punc_st = '[,.;:?!]'
texts_re3 = [sub(punc_st, '', t) for t in texts_re2]
print(texts_re3) # ['afabasabag', 'abtta $$a', 'uysfsfaa&***$']


# 단계4 : 특수문자 제거
spec_st = '[@#$%^&*()]'
texts_re4 = [sub(spec_st, '', t) for t in texts_re3]
print(texts_re4) # ['afabasabag', 'abtta a', 'uysfsfaa']

# 단계5 : 공백제거 : '구분자'.join(word)
texts_re5 = [ ''.join(t.split())  for t in texts_re4]
print(texts_re5) # ['afabasabag', 'abttaa', 'uysfsfaa']


# exam04





