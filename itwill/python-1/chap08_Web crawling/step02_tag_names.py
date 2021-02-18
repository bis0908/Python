# -*- coding: utf-8 -*-
"""
step02_tag_names

@author: wonseok
"""

from bs4 import BeautifulSoup
import os

os.chdir('E:\Code\Python\itwill\chap08_Web crawling\data')

file = open('html01.html', mode = 'r', encoding = 'utf-8')
src = file.read()
type(src)

html = BeautifulSoup(src, 'html.parser')
print(html)
type(html)
html.select('ul>li')

h1 = html.html.body.h1
print('h1:', h1.string)

h2 = html.find('h2')
print('h2:', h2.string)

lis = html.find_all('li')
print(lis)
