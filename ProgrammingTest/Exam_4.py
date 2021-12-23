# 재귀호출을 반복문으로 치환하면 될 것 같습니다.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(1000))