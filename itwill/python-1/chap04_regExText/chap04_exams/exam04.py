'''
문4) 다음 texts 객체를 대상으로 단계별로 텍스트를 전처리하시오.


 <텍스트 전처리 후 결과>
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''

# 전처리 전 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']


from re import sub

print('전처리 전 : ', texts)
texts_re = []
# 1. 소문자 변경
texts_re = [t.lower() for t in texts]

# sub(pattern, repl, string)

# 2. 숫자 제거
special_text = '[0-9,a-z.A-Z:;?~@#$%^&*()_+]'
texts_re2 = [sub(special_text, '', t) for t in texts_re]
# 3. 문장부호 제거
texts_re3 = [' '.join(t.split()) for t in texts_re2]
print(texts_re3)
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고!', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']




# 4. 영문자 제거

# 5. 특수문자 제거

# 6. 공백 제거(2칸 이상 공백 -> 1칸 공백)

