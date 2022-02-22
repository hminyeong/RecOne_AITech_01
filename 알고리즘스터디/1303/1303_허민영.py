#BFS 너비 우선 탐색

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(color, a, b):
    #n = len(graph)
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] != 0 and graph[nx][ny] == color:
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1
        if count == 0:
            count = 1
    return count


m, n = map(int, input().split()) #행 열
graph = []
for _ in range(n):
    a = list(input())
    graph.append(a)
#print(graph)

white, blue = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            if graph[i][j] == 'W':
                white += bfs(graph[i][j],i,j)**2
            else:
                blue += bfs(graph[i][j],i,j)**2

print(white, blue)
