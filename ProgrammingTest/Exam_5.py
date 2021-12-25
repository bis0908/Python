
# 맵 크기 공백 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 지도 배열
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
isNext = True
while isNext:
    isNext = False # 수행할 내용이 없을경우 반복문 이탈
    for i in range(n):
        for j in range(m):
            # 탐색 제한 조건
            if i == 0 or i == len(graph[0])-1:
                continue
            elif j == 0 or j == len(graph)-1:
                continue
            else:
                # 상하좌우
                top = graph[i-1][j]
                left = graph[i][j-1]
                right = graph[i][j+1]
                bottom = graph[i+1][j]
                # 상하좌우가 현재 셀보다 크거나 같을 경우
                if top >= graph[i][j] and left >= graph[i][j] and \
                        right >= graph[i][j] and bottom >= graph[i][j] and 0 != graph[i][j] :
                    graph[i][j] = (graph[i][j])+1   # 현재 셀 증가
                    isNext = True
                else:
                    graph[i][j] = graph[i][j]

# 처리 결과 보여주기
for i in range(len(graph)):
    print(graph[i])
    for j in range(len(graph[0])):
        result += graph[i][j]
print("연못 물 깊이의 총 합은 {} 입니다".format(result))