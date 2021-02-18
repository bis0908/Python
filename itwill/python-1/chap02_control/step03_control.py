# -*- coding: utf-8 -*-
"""
제어문: 조건문(if) + 반복문(while, for)


"""

# 조건문(if)

import datetime

today = datetime.datetime.now()
print(today)

day = today.weekday()
print(day)

if day >= 5:
    print('today is weekend')
else:
    print('today is weekday')

# keyboard input: 100 ~ 85 'good', 84 ~ 70: 'normal', under 70: 'low''

score  = int(input('Record your score! (0 ~ 100): '))

if score >= 85 and score <=100:
    print('High-score~')
elif score >= 70:
    print('you can do it better!')
else:
    print('dumb-ass~')



# ***
y_true = [1, 0, 1, 0, 1]
y_pred = [1, 0, 0, 0, 1]

size = len(y_true)

acc = 0 # 분류 정확도

for i in range(size):
    if y_true[i] == y_pred[i]:
        fit = int(y_true[i] == y_pred[i])
        acc += fit * 0.2 # acc = acc + 누적값

print('분류 정확도 = %.2f%%'%acc)

# 구구단 출력
for i in range(2, 10):
    print(f'~~ {i} 단 ~~')
    for j in range(1, 10):
        print('%d * %d = %d'%(i, j, i*j))

