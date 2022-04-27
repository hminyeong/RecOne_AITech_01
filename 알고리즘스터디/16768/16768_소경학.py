from collections import deque
n, k = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(input()))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def search_cnt(xx,yy,num):
    q = deque()
    q.append((xx,yy))
    cnt = 1
    visit[xx][yy] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<10 and array[nx][ny] == num and visit[nx][ny] == False:
                cnt += 1
                visit[nx][ny] = True
                q.append((nx,ny))
    return cnt

def change_zero(xx,yy,num):
    q = deque()
    q.append((xx,yy))
    array[xx][yy] = '0'
    visited[xx][yy] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<10 and array[nx][ny] == num and visited[nx][ny] == False:
                array[nx][ny] = '0'
                visited[nx][ny] = True
                q.append((nx,ny))
t = 0
while True:
    t += 1
    visit = [[False for _ in range(10)] for _ in range(n)]
    crray = [[0 for _ in range(10)] for _ in range(n)]
    visited = [[False for _ in range(10)] for _ in range(n)]
    check = 0
    for i in range(n):
        for j in range(10):
            if visit[i][j] == False and array[i][j] != '0':
                crray[i][j] = search_cnt(i,j,array[i][j])
                if crray[i][j] >= k:
                    check = 1
    if check == 0:
        break
    for i in range(n):
        for j in range(10):
            if crray[i][j] >= k and array[i][j] != '0':
                change_zero(i,j,array[i][j])
    for i in range(n-1,0,-1):
        for j in range(10):
            if array[i][j] == '0':
                for kk in range(i-1,-1,-1):
                    if array[kk][j] != '0':
                        array[i][j], array[kk][j] = array[kk][j], '0'
                        break
for i in array:
    print("".join(i))