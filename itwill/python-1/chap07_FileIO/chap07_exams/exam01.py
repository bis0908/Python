#문제1) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오.

'''
문단 내용
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문장 수 :  6

단어 내용
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''
import os
#os.chdir('C:/ITWILL/3_Python-I/workspace/chap07_FileIO/data/')

file = open("ftest.txt", mode = 'r')

lines = file.readlines()

sents = []

for line in lines:
    sents.append(line.strip())

print(sents)
print('문장 수: ', len(sents))


words = []
for line in sents:  # 문장 생성
    for word in line.split():   # 단어 생성
        words.append(word)

print(words)
print('단어 수', len(words))
