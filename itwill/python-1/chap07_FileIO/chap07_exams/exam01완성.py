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
os.chdir('C:/ITWILL/3_Python-I/workspace/chap07_FileIO/data/')

file = open("ftest.txt", mode = 'r')

# 줄 단위 전체 읽기 
lines = file.readlines() # list

sents = [] # 문장 save 
for line in lines : # list -> 원소 
    sents.append(line.strip()) # 줄바꿈 제거 > list
print('문단 내용')
print(sents)
print('문장 수 : ', len(sents))

words = [] # 단어 save 
for line in sents : # 문장 생성 
    # 'programming is fun' -> 3개 단어 
    for word in line.split() : # 단어 생성
        words.append(word)

print('단어 내용')
print(words)
print('단어 수 :', len(words))


# 문장 + 단어 생성 
sents = []
words = []
for line in lines : # 문장 생성 
    sents.append(line.strip())        
    for word in line.split() : # 단어 생성
        words.append(word)
        
print(sents)
print(words)        
        
















