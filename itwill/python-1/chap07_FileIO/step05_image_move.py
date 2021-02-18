# -*- coding: utf-8 -*-
"""
step05_image_move

<file 관리 모듈 & 이진 파일 Read/Write>
 특정 디렉토리에 *.png -> 다른 디렉토리로 이동



@author: wonseok
"""

import os # dir of file path
from glob import glob # *, ?

# image 파일 경로
os.chdir('E:\Code\Python\itwill\chap07_FileIO')

file_path = 'data2/' # raw file dir
file_path2 = 'images/' # image move dir

# dir 존재 유무 판단

if os.path.exists(file_path):
    print('해당 디렉토리 있음')

    # image 저장 디렉토리 생성
    # os.mkdir(file_path2)
    images = [] # png 파일 name 저장

    # dimage 디렉토리에서 *.png 검색
    for pic_path in glob(file_path + '*.png'): #data2/*.png
        print(pic_path) # path/101.png

        # 경로와 파일명 분리
        img_path = os.path.split(pic_path)
        images.append(img_path[1])

        # 이진 파일 읽기
        rfile = open(pic_path, mode = 'rb')
        output = rfile.read()

        # 이진 파일 쓰기
        wfile = open(file_path2+img_path[1], mode = 'wb')
        wfile.write(output)

    wfile.close(); rfile.close()
    print('~~image 파일 이동 성공~~')
else:
    print('해당 디렉토리 없음')



'''
data2 -> txt01_data.txt ~ txt05_data.txt'
txt_file_total 변수에 저장하기
'''

txt_file_total = []

# data2 디렉토리에서 txt file 검색
for txt_path in glob(file_path + '*.txt'):
    print(txt_path)

    rfile = open(txt_path, mode = 'r')
    texts = rfile.read()
    txt_file_total.append(texts)

rfile.close()
print(txt_file_total[0], type(txt_file_total), len(txt_file_total))


# 한 개 변수에 누적
txt_total = ''

for texts in txt_file_total:
    txt_total += texts

print(txt_total)
