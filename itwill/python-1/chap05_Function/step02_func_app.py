# -*- coding: utf-8 -*-
"""
step02_func_app

함수 응용 
"""

# 1. 텍스트 전처리 함수  

# 텍스트 전처리 : file
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']
print('전처리 전 ')
print(texts)

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
    texts_re5 = [ ''.join(t.split())  for t in texts_re4]
    
    return texts_re5

# 함수 호출 
texts_re = clean_texts(texts)
print('전처리 후 ')
print(texts_re)


# 2. 표본의 분산/표준편차 
dataset = [2, 4, 5, 6, 1, 8]
len(dataset) # 6

'''
분산 = sum((x - mu)**2) / n-1
표준편차 = sqrt(분산)
'''

from statistics import sqrt, variance, stdev  
# 평균, 제곱근, 분산,표준편차 

print('분산 = ', variance(dataset))
print('표준편차 =', stdev(dataset))
'''
분산 =  6.666666666666666
표준편차 = 2.581988897471611
'''

# 산술평균 
def avg(data) :  
    a = sum(data) / len(data)
    return a


print('평균 =', avg(dataset))
# 평균 = 4.333333333333333


# 분산/표준편차 
def var_std(data) :
    a = avg(data) # 산술평균 
    
    # list + for : (x - mu)**2
    diff = [(x-a)**2  for x in data]
    var = sum(diff) / (len(data) - 1) # 분산 
    std = sqrt(var) # 표준편차 
    
    return var, std
    

var, std = var_std(dataset)
print('var =', var)
print('std = ', std)

'''
var = 6.666666666666666
std =  2.581988897471611
'''














    


