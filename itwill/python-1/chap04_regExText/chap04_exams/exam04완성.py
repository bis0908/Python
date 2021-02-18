'''
문4) 다음 texts 객체를 대상으로 단계별로 텍스트를 전처리하시오. 


 <텍스트 전처리 후 결과> 
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''

# 전처리 전 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

from re import sub

print('전처리 전 : ', texts)

# 1. 소문자 변경
texts_re = [t.lower() for t in texts ]
print('texts_re :', texts_re)   

# 2. 숫자 제거 
texts_re2 = [ sub('[0-9]', '', text)   for  text in texts_re  ]
print('texts_re2 :', texts_re2)


# 3. 문장부호 제거 
punc_str = '[,.?!:;]'

texts_re3 = [ sub(punc_str, '', text) for text in  texts_re2 ]
print('texts_re3 :', texts_re3)

# 4. 영문자 제거 
texts_re4 = [ sub('[a-z]', '', text)   for  text in texts_re3  ]
print('texts_re4 :', texts_re4)

# 5. 특수문자 제거 
spec_str = '[!@#$%^&*()]'

texts_re5 = [ sub(spec_str, '', text) for text in texts_re4]
print('texts_re5 :', texts_re5)

# 6. 공백 제거 
texts_re6 = [ ' '.join(text.split())  for text in texts_re5]
print('texts_re6 :', texts_re6)

