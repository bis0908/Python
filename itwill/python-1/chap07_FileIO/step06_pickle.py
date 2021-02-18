# -*- coding: utf-8 -*-
"""
step06_pickle

pickle
 - list, dict 객체를 binary 형태로 저장(저용량)

@author: wonseok
"""

import os

os.chdir('E:\Code\Python\itwill\chap07_FileIO\data')

words = []

rfile = open('texts_write.txt', mode = 'r', encoding = 'utf-8')

lines = rfile.readlines()

words = [word for line in lines for word in line.split()]
rfile.close()
import pickle # object -> file(binary) -> load

# save
wfile = open('words.pickle', mode = 'wb')
pickle.dump(words, wfile)
print('pickle file saved')
wfile.close()

# load
rfile = open('words.pickle', mode = 'rb')
words_pickle = pickle.load(rfile)
print(words_pickle)
rfile.close()




