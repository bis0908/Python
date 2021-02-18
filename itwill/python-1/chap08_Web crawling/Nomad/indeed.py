# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:08:44 2021

Nomadcoders - python scrapping

@author: wonseok
"""

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


lst = []



# url이 바뀔 때마다 page 넘버 스크랩
for num in range(0, 12):
    print('collecting page numbers...', num)
    # num *= 50
    indeed_result = requests.get(f'https://kr.indeed.com/jobs?q=data+engineer&limit=50&start={num}')
    indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
    # pagination = indeed_soup.find('div', {'class': 'pagination'}).find_all('b')
    pagination = indeed_soup.find('div', {'class': 'pagination'}).select('li > b')
    for page in pagination:
        lst.append(page.string)

li = indeed_soup.find('div', {'class': 'pagination'}).find_all('a')
paging = []
for l in li:
    paging.append(l.get('aria-label'))

len(pagination)
# for page in pages:
#     spans.append(page.find('span'))

# spans = spans[:-1]
