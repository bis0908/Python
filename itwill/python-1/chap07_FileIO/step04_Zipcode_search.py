# -*- coding: utf-8 -*-
"""
step04_Zipcode_search



@author: wonseok
"""
### 동 입력 -> 우편번호 검색 시스템
import os
os.chdir('E:\Code\Python\itwill\chap07_FileIO\data')

try:
    dong = input('동 입력 (ex. 우만동): ')

    # 우편 번호 파일 읽기
    file = open('zipcode.txt', mode = 'r', encoding = 'utf-8')
    line = file.readline() # 첫 줄 읽기
    # print(line) # ﻿135-806	서울	강남구	개포1동 경남아파트		1

    cnt = 0
    while line != '':
        token = line.split('\t') # tab key Split
        # print(token) # ['\ufeff135-806', '서울', '강남구', '개포1동 경남아파트', '', '1\n']

        if token[3].startswith(dong): # 사용자 입력단 접두어와 비교
            print('['+token[0]+']', token[1], token[2], token[3], token[4])
            cnt += 1

        line = file.readline() # 2줄 ~ 끝 줄

    print('Result :', cnt)



except Exception as e :
    print('예외 발생 : ', e)


finally :
    file.close()
