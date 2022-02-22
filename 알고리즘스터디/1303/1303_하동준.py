import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(m)]

def dfs(x, y, std, count):
    graph[x][y] = 'visited'
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] != 'visited' and graph[nx][ny] == std:
                count = dfs(nx, ny, std, count + 1)
    return count


white, blue = 0, 0

for i in range(m):
    for j in range(n):
        if graph[i][j] != 'visited':
            if graph[i][j] == 'W':
                white += dfs(i, j, 'W', 1)**2
            else:
                blue += dfs(i, j, 'B', 1)**2

print(white, blue)
