# -*- coding: utf-8 -*-
"""
step02_text file

open('path/~')

@author: wonseok
"""

import os
os.chdir('E:\Code\Python\itwill\chap07_FileIO\data')

try:
    print('현재 경로', os.getcwd())
    file = open('ftest.txt', mode = 'r')
    print(file.read()) # ftest.txt 전체 내용 출력
    file.close() # file obj close

    file2 = open('ftest2.txt', mode = 'w') # 처음부터 쓰기
    file2.write('my first text')
    file2.close()

    file3 = open('ftest2.txt', mode = 'a') # 끝에 내용 추가
    file3.write('\nmysecond text')
    file3.close()

    '''
    file.read(): 전체 문서 읽기
    file.readline(): 한 줄 읽기
    file.readlines(): 줄 단위 전체 읽기
    '''

    # 줄 단위 읽기
    print('줄 단위 읽기')
    file4 = open('ftest.txt', mode = 'r')
    line = file4.readline()

    while line != '':
        print(line)
        line = file4.readline()

    print('줄 단위 전체 읽기')
    file5 = open('ftest.txt', mode = 'r')
    lines = file5.readlines()
    print(lines) # ['programming is fun\n', 'very fun!\n', 'have a good time\n', 'mouse is input device\n', 'keyboard is input device\n', 'computer is input output system']
    print(type(lines), len(lines)) # <class 'list'> 6

    # 줄 단위 읽기 > 출력
    for line in lines:
        print(line.strip()) # strip(): 문장 끝 불용어 제거(줄바꿈, 공백)

    # with문 File I/O; close가 자동!
    with open('ftest2.txt', mode = 'r') as rfile:
        lines = rfile.read()
        print(lines)

    with open('ftest3.txt', mode = 'w', encoding = 'utf-8') as wfile:
        wfile.write('파이썬 파일 작성 연습 11')
        wfile.write('\n파이썬 파일 작성 연습 22')

    file6 = open('ftest3.txt', mode = 'r', encoding = 'utf-8')

except Exception as e:
    print("Error Occur: ", e)


finally:
    pass
