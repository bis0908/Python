# 문5) 다음과 같이 단 수를 인수로 넘겨서 해당 구구단을 장식하여 함수 장식자를 정의하시오.
'''
*** 2단 ***
2 * 1 = 2
2 * 2 = 4
   :
2 * 9 = 18
***********
'''

def gugu_deco(func):
    def inner(dan):
        print('*** {}단 ***'.format(dan))
        func(dan)
        print('*' * 11)
    return inner

@gugu_deco
def gugu_dan(dan):
    for i in range(1, 10) :
        print('%d * %d = %d'%(dan, i, dan*i))

gugu_dan(2)
