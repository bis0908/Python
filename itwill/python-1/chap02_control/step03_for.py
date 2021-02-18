# -*- coding: utf-8 -*-
"""
step03_for

반복문(for)

형식)
for 변수 in 열거형객체 : 
    실행문
    실행문
    
열거형객체 : iterable -> 반복가능(vector 변수)     
 -> string, list, tuple, set, dict 
"""

# 1. 문자열(string) 이용 
string = "나는 홍길동 입니다."
print(len(string)) # 11 
string[0]

# 문자 크기 = 반복수 
for s in string :
    print(s, end = ' ') # 나 는   홍 길 동   입 니 다 . 

print() # line skip     

# 단어 크기 = 반복수     
for w in string.split() : 
    print(w, end = ' ') # 나는 홍길동 입니다.
    
  
# 2. list 이용 
# 형식) [원소1, 원소2, ... 원소n] - 1차원 
lst = [10,20,30,40,50]
print(len(lst)) # 5

lst2 = [] # 빈 list

for i in lst : # 5회 반복 
    print(i, end = ' ') # 10 20 30 40 50
    re = i * 0.5
    #print(re, end = ' ') # 5.0 10.0 15.0 20.0 25.0
    lst2.append(re) # 원소 추가 
    
# for end
print(lst2) # [5.0, 10.0, 15.0, 20.0, 25.0]   
    
  
# 3. range 이용     
help(range)
# Help on class range in module builtins:  
'''
range(stop) : 0 ~ stop-1 정수 
range(start, stop) : start ~ stop-1 정수
range(start, stop[, step]) : start ~ stop-1, step 증감 
'''    

for num in range(10) : # 0 ~ 9
    print(num, end = ' ') # 0 1 2 3 4 5 6 7 8 9 

for num in range(1, 11) : # 1 ~ 10
    print(num, end = ' ') # 1 2 3 4 5 6 7 8 9 10
    
for num in range(1, 11, 2) : # 1 ~ 10
    print(num, end = ' ') # 1 3 5 7 9 
    
for num in range(11, 1, -2) : # 11 ~ 2
    print(num, end = ' ') # 11 9 7 5 3    
    
  
# 4. range + list 이용 
print(range(1, 6)) # range(1, 6)

# range 객체 -> 숫자 추출 
print(list(range(1, 6))) # [1, 2, 3, 4, 5]


lst = list(range(1, 101))
print(lst)
print('lst 길이 : ', len(lst)) # lst 길이 :  100

lst_re = [] # 빈 list : 5의 배수 저장 

# 1~100까지 5의 배수만 추출 -> lst_re 저장  
for n in lst :
    if n % 5 == 0 :
        lst_re.append(n) # 원소 추가 
        
# for end 
print('lst_re : ', lst_re)
print('size =', len(lst_re)) # size = 20


# 문) 50~200 사이 숫자를 lst2로 만들고, 3의 배수만 추출하여 lst_re2 추가   
lst2 = list(range(50,201)) 
print(lst2)      

lst_re2 = [] # 빈 list : 3의 배수 저장 

for n in lst2 :
    if n % 3 == 0 :
        lst_re2.append(n) # 원소 추가 
        
# for end
print('3의 배수 : ', lst_re2) 
print(len(lst_re2)) # 50      
        
        
# 분류정확도(accuracy)
y_true = [1, 0, 1, 0, 1] # list
y_pred = [1, 0, 0, 0, 1] # list 

print(y_true[0] == y_pred[0]) # True
        
size = len(y_true)    

acc = 0 # 분류정확도 
for i in range(size) : # index : 0 ~ 4 
    if y_true[i] == y_pred[i] :
        fit = int(y_true[i] == y_pred[i]) # T/F -> 1/0 
        acc += fit * 0.2 # acc = acc + 누적값

print("분류정확도 = %.2f%%"%acc) # 분류정확도 = 0.80%











    
    
    
    
    
    