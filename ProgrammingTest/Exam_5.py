
# 맵 크기 공백 구분하여 입력받기
n, m = map(int, input().split())
chk = [[False] * m for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
isNext = True
while(isNext):
    isNext = False
    for i in range(n):
        for j in range(m):
            if i == 0 or i == len(graph[0])-1:
                continue
            elif j == 0 or j == len(graph)-1:
                continue
            else:
                top = graph[i-1][j]
                left = graph[i][j-1]
                right = graph[i][j+1]
                bottom = graph[i+1][j]
                if top >= graph[i][j] and left >= graph[i][j] and \
                        right >= graph[i][j] and bottom >= graph[i][j] and 0 != graph[i][j] :
                    graph[i][j] = (graph[i][j])+1
                    isNext = True
                else:
                    graph[i][j] = graph[i][j]

for i in range(len(graph)):
    print(graph[i])
    for j in range(len(graph[0])):
        result += graph[i][j]
print("연못 물 깊이의 총 합은 {} 입니다".format(result))