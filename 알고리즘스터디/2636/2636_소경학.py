from collections import deque
import copy
n, m = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def solve(array):
    visit = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0,0))
    visit[0][0] = True
    while q:
        xx,yy = q.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if array[nx][ny] == 0 and visit[nx][ny] == False:
                    visit[nx][ny] = True
                    q.append((nx,ny))

    cnt = 0
    check = copy.deepcopy(array) 
    for i in range(1,n-1):
        for j in range(1,m-1):
            if array[i][j] == 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if array[nx][ny] == 0 and visit[nx][ny] == True:
                        cnt += 1
                        check[i][j] = 0
                        break
    return check, cnt
nn = 0
t = 0
while True:
    chk = False
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                chk = True
    if chk == False:
        break
    array, nn = solve(array)
    t += 1
print(t)
print(nn)
