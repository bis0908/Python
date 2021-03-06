# -*- coding: utf-8 -*-
"""
step05_image_reshape


- image shape & reshape
- newaxis 속성: 차원 추가

@author: wonseok
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# 1. dataset load
digits = load_digits() # 글자 이미지가 digit 형태로 보관되어 있다

# 입력변수(x): 숫자(0~9) 필기체의 흑백 이미지
# 결과변수(y): 정답(10진수 정수: 0~9)

x = digits.data
y = digits.target

x.shape # (1797, 64) - (size, 64(h:8 * w:8))
y.shape # (1797, )
y # [0, 1, 2, ..., 8, 9, 8]


# 2. image reshape
# 첫번째 image
first_img = x[-1]
first_img
first_img.shape # (64, ) -> 8x8

img2d = first_img.reshape(8, 8)
img2d.shape

# 이미지 시각화
plt.imshow(img2d, cmap = 'gray')


# 정답
y[-1]


# 3. newaxis 속성: 새로운 차원 추가
x.shape # (1797, 64) <- 2d
x3d = x.reshape(-1, 8, 8) # 3d (size, h, w)
x3d.shape

# image shape: (size, h, w, c) <- 4d
x4d = x3d[:,:,:,np.newaxis]
x4d.shape

# 마지막 image
plt.imshow(x4d[-1], cmap = 'gray')

y[:10]

# image 행렬 시각화(2x5)
plt.figure(figsize = (15, 8))

for i in np.arange(10):
    plt.subplot(2, 5, i+1)
    plt.title('{}'.format(y[i]))
    plt.axis('off')
    plt.imshow(x4d[i], cmap = 'gray')

# 칼럼 image read & show
path = 'C:/Users/sucki/Downloads/Chrome_Image/'
img = plt.imread(path + 'unnamed.jpg')
img.shape # (1024, 759, 3): (height, weight, color)

plt.imshow(img)
img # dtype=uint8

# rgb 색상 추출
red_img = img[:,:,0]
green_img = img[:,:,1]
blue_img = img[:,:,2]

plt.imshow(red_img)
plt.imshow(green_img)
plt.imshow(blue_img)
