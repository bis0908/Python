'''
문1) Start counter 문제

height : 3 <- 키보드 입력
*
**
***
start 개수 : 6
'''

# 함수 정의
def StarCount(height):
    s_cnt = 0 # 별 개수 카운트

    ## 내용 채우기 ##
    for s_cnt in range(height):
        print('*' * (s_cnt + 1))
    return s_cnt + 1

# 함수 호출
star_cnt = StarCount(int(input('height : '))) # 층 수 입력

# start 개수 출력
print('start 개수 : %d'%star_cnt)
