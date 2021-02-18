'''
 문6) 패토리얼(Factorial) 계산 함수를 정의하시오.
     예) 5! -> 5*4*3*2*1 : 120
'''

def Factorial(n):
    if n == 0:
        return 1
    else:
        result = n * Factorial(n-1)
        return result


result_fact = Factorial(5)
print()
print('패토리얼 결과:', result_fact) #  패토리얼 결과: 120


