# -*- coding: utf-8 -*-
"""
step05_images_move.py

<file 관리 모듈 & 이진파일 읽기/쓰기> 
 특정 디렉터리에 *.png -> images 디렉터리 이동
"""

import os # dir of file path 
from glob import glob # *, ? -> *.png : 파일 패턴 검색 

# 1. image 파일 경로 
os.chdir('C:/ITWILL/3_Python-I/workspace/chap07_FileIO/')
file_path = 'data2/' # 원본 file 디렉터리
file_path2 = 'images/' # images 이동 디렉터리 

# 2. 디렉터리 존재 유무 
if os.path.exists(file_path) :
    print('디렉터리 있음')
    
    # 3. image 저장 디렉터리 생성 
    #os.mkdir(file_path2) # images 디렉터리 생성 
    images = [] # png 파일 저장 
    
    # 4. image 디렉터리에서 *.png 검색 
    for pic_path in glob(file_path + '*.png') : # data2/*.png
        print(pic_path) # 'data2/101.png'
        # 5. 경로와 파일명 분리 
        img_path = os.path.split(pic_path)#'data2', '101.png'
        images.append(img_path[1])
        
        # 6. 이진파일 읽기
        rfile = open(pic_path, mode='rb') # image read 
        output = rfile.read() # image 읽기 
        
        # 7. 이진파일 쓰기 : images/101.png 
        wfile = open(file_path2+img_path[1], mode='wb')
        wfile.write(output)
        
    #print('images :', images)
    wfile.close(); rfile.close()
    print('~~image 파일 이동 성공~~')    
    
else :
    print('해당 디렉터리 없음')

################################################
###  data2 -> txt01_data.txt ~ txt05_data.txt  
###   txt_file_total 변수에 저장하기 
################################################



    
    
    
    
    
    
    
    
    
    
    
    
    



