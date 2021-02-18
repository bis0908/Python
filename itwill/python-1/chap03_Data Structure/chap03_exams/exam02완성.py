'''
step02 문제

문1) message에서 'spam' 원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.
      <조건> list + for 형식1) 적용   
      
  <출력결과>      
[1, 0, 1, 0, 1]   


문2) message에서 'spam' 원소만 추출하여 spam_list에 추가하시오.
      <조건> list + for + if 형식2) 적용   
      
  <출력결과>      
['spam', 'spam', 'spam']   
'''

message = ['spam', 'ham', 'spam', 'ham', 'spam']

# 문제1]
#dummy = [ 실행문 for msg in message]
dummy = [ 1 if msg == 'spam' else 0 for msg in message]
# 실행문 : if문 3항 연산자 이용  
print(dummy) # [1, 0, 1, 0, 1]

# 문제2]
spam_list = [ msg for  msg in message  if msg == 'spam']
print(spam_list) # ['spam', 'spam', 'spam']
