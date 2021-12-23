# 연못 크기 공백 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 주어진 범위를 벗어날 시 종료
    if x <= -1 or x >= n or y <=-1 or y >= m:
        return False

    # 상하좌우를 비교하려면 현재 셀은 상하좌우 셀이 모두 있는 경우에만 해당. 즉 (1,1) ~ (8,8)
    # 만약 현재 셀의 상하좌우 모두의 깊이가 자신보다 같거나 크다면
    if graph[x][y] <= (graph[x-1][y] * graph[x][y-1] * graph[x+1][y] * graph[x][y+1]):
        graph[x][y] += 1 # 현재 셀 깊이 증가
        return True
    return False

# 모든 물 깊이의 합
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if 1 <= i <= 8 and 1 <= j <= 8:
            dfs(i, j)
            result += dfs(i,j)
print(result)
