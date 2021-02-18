# -*- coding: utf-8 -*-
"""
리스트 내포 : list + for 
 - list에서 for문 사용 
 형식1) 변수 = [실행문  for]
  실행순서 : 1.for > 2.실행문 > 3. 변수 저장 
 형식2) 변수 = [실행문  for if]  
  실행순서 : 1.for > 2. if > [3.실행문 > 4. 변수 저장]
"""

# 형식1) 변수 = [실행문  for]

# x변량에 제곱(**) 연산 
x = [2, 4, 1, 5, 7]

#x ** 2 # TypeError:

# 일반 for문 
lst = []     
for i in x :
    #print(i**2)
    lst.append(i**2)
    
print(lst) # [4, 16, 1, 25, 49]

# list + for 
lst = [i**2  for i in x]
print(lst) # [4, 16, 1, 25, 49]


# 형식2) 변수 = [실행문  for  if]

# 1~100사이에서 5의 배수 추출 
num = list(range(1, 101))
print(num)

num2 = [i for i in num  if i % 5 == 0] # 형식2)
print(num2)

# 형식1) 변수 = [실행문  for]
num3 = ['5의 배수' if i % 5 == 0 else i for i in num]
print(num3)

# list + for + 내장함수 
a = [[1,2,3], [10,20,30], [100,200,300]] # 중첩 list 
print(len(a)) # 3 

a_sum = [sum(i) for i in a]
print(a_sum) # [6, 60, 600]
    
# exam02








