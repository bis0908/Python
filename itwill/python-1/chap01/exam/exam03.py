'''
step03 문제
'''

'''
문) 3개의 단어를 키보드로 입력 받아서 각 단어의 첫자를 추출하여 단어의 약자를 출력하시오.
  조건1) 각 단어 저장 변수 : word1, word2, word3
  조건2) 입력과 출력 구분선 : 문자열 연산
  조건3) 약자를 저장 변수 : abbr
  조건4) 원래 단어 저장 변수 : words

   <<화면출력 결과>>
 첫번째 단어 : Korea
 두번째 단어 : Baseball
 세번째 단어 : Orag
 =================
 약자 : KBO
 원래 단어 : Korea Baseball Orag
'''

ch1 = str(input('문자열 입력 1/3: '))
ch2 = str(input('문자열 입력 2/3: '))
ch3 = str(input('문자열 입력 3/3: '))
print('=' * 30)

abbr = ch1[0] + ch2[0] + ch3[0]
long = ''.join(ch1+' '+ch2+ ' '+ch3)


print('약자: {}'.format(abbr))
print('원래 단어: {}'.format(long))

# escape 문자: \n, \t, \b, \r, '', "" -> 문자열 제어

print('test')
print('\nexcape') # 한줄 더 띄워서 표시
print('\\nexcape')
print(r'\nexcape')

print('e:\ITWill\test') # e:\ITWill	est
print('e:\ITWill\\test') # e:\ITWill\test
print('e:\ITWill\test') # e:\ITWill\test