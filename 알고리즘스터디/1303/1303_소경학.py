from collections import deque
m, n = map(int,input().split())

array = []
for _ in range(n):
    array.append(list(input()))
q = deque()
visit = [[False for _ in range(m)] for _ in range(n)]
W, B = 0, 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for a in range(n):
    for b in range(m):
        if visit[a][b] == False:
            if array[a][b] == 'W':
                visit[a][b] = True
                Wcnt = 1
                q.append([a,b])
                while q:
                    x,y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0<=nx<n and 0<=ny<m:
                            if visit[nx][ny] == False and array[nx][ny] == 'W':
                                visit[nx][ny] = True
                                Wcnt += 1
                                q.append([nx,ny])
                W += Wcnt**2
            else:
                visit[a][b] = True
                Bcnt = 1
                q.append([a,b])
                while q:
                    x,y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0<=nx<n and 0<=ny<m:
                            if visit[nx][ny] == False and array[nx][ny] == 'B':
                                visit[nx][ny] = True
                                Bcnt += 1
                                q.append([nx,ny])
                B += Bcnt**2

print(W,B)




