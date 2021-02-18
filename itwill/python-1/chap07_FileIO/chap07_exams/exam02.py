'''
문제2) 서울 지역을 대상으로 '동' 이름만 추출하여 다음과 같이 출력하시오.
  단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
  단계2 : 중복되지 않은 전체 '동' 개수 출력 : list -> set -> list

  <출력 예시>
서울시 전체 동 개수 =  797
'''
import os
os.chdir('E:\Code\Python\itwill\chap07_FileIO\data')

try:
    file = open('zipcode.txt', mode = 'r', encoding = 'utf-8')
    line = file.readline() # 첫 줄 읽기
    dong = []
    while line != '':
        token = line.split('\t') # tab key Split
        if token[1] == '서울':
            d = token[3].split()
            dong.append(d[0])
        line = file.readline()


    ldong = list(set(dong))
    print('서울시 전체 동 개수:', len(ldong))



except Exception as e :
    print('예외 발생 : ', e)

