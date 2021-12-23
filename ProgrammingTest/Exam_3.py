def factorial(num):
    if num == 1:    # n이 1일 때 1을 반환하고 재귀호출 탈출
        return 1
    return num * factorial(num - 1)

print(factorial(4)) # 24
