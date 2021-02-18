# -*- coding: utf-8 -*-
"""
step03_texts_preprocessing.py

file -> line(sentence) -> 전처리 

<작업 절차>
1. file read/전처리 
2. file save
3. word count
"""

import os 

# 구분자 : \\ or /
os.chdir('C:\\ITWILL/3_Python-I/workspace/chap07_FileIO/data')
print(os.getcwd())
# C:\ITWILL\3_Python-I\workspace\chap07_FileIO\data

# 텍스트 전처리 : chap05 > step02 
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
    spec_st = '[@#$%^&*()]'
    texts_re4 = [sub(spec_st, '', t) for t in texts_re3]
        
    # 단계5 : 공백제거 : 2칸 이상 공백 -> 1칸 공백 
    texts_re5 = [ ' '.join(t.split())  for t in texts_re4]
    
    return texts_re5

try :
    # 1. file read/전처리 
    rfile = open('texts.txt', encoding='utf-8') # mode='r'
    #print(rfile.read())  
    
    # 줄 단위 전체 읽기 
    texts = rfile.readlines()
    print('텍스트 전처리 전')
    print(texts) # list
    
    # texts 전처리 : list + for  
    texts_re = [row.strip() for row in texts] # 줄바꿈 제거   
    
    texts_re = clean_texts(texts_re) # 전처리 함수 호출 
    print('텍스트 전처리 후 ')
    print(texts_re)
    print('문장 길이 : ', len(texts_re))
    
    # 2. file save
    '''
    wfile = open('texts_write.txt',mode='w',encoding='utf-8')
    for texts in texts_re :
        wfile.write(texts + '\n') # file save 
        
    print('text file saved...')
    '''
    
    # 3. word count
    words = [] # 단어 save 
    wc = {} # 단어 출현빈도수 save 
    rfile2 = open('texts_write.txt',mode='r',encoding='utf-8')
    
    texts = rfile2.readlines() # 줄 단위 읽기 
    
    # word 추출 
    for row in texts :
        for word in row.split() : # 공백 기준 split
            words.append(word) # 단어 생성 
            
    print('words :', words, len(words)) #  19
    
    # word count 
    for word in words :
        wc[word] = wc.get(word, 0) + 1
        
    print(wc) # dict 
    
    # 최고 출현 단어 
    print('max =', max(wc, key = wc.get)) # max = 우리나라
    # 출현빈도수 기준 단어 내림정렬 
    wc_sorted = sorted(wc, key=wc.get, reverse=True)
    print(wc_sorted) # list 반환
    
    # top word 
    print('top5 word : ', wc_sorted[:5]) # index 사용 
    # top5 word :  ['우리나라', '대한민국', '나는', '만세', '비아그라']    
    
    # 단어(top5) vs 출현빈도수 
    for word in wc_sorted[:5] :
        print(word, wc[word], sep=' -> ') # key -> value
        
    '''
    우리나라 -> 2
    대한민국 -> 2
    나는 -> 2
    만세 -> 1
    비아그라 -> 1
    '''      
    
except Exception as e :
    print('예외 발생 : ', e)
finally :
    rfile2.close() ;rfile.close() #wfile.close();  # 객체 닫기 : 역순  













