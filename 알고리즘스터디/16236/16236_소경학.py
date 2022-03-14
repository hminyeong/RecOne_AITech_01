from collections import deque
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x = i
            now_y = j
array[now_x][now_y] = 0
q = deque()
q.append((now_x,now_y,0))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
start = 2
def BFS(start):
    visit = [[False for _ in range(n)] for _ in range(n)]
    visit[now_x][now_y] = True
    eat = []
    while q:
        x,y,z = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and array[nx][ny] <= start:
                if visit[nx][ny] == False:
                    if array[nx][ny] < start and array[nx][ny] != 0:
                        visit[nx][ny] = True
                        eat.append([nx,ny,z+1])
                    else:
                        visit[nx][ny] = True
                        q.append((nx,ny,z+1))
    if len(eat) == 0:
        return -1,-1,-1
    else:
        eat.sort(key=lambda x:(x[2],x[0],x[1]))
        return eat[0][0],eat[0][1],eat[0][2]
cnt = 0
time = 0
while True:
    
    if cnt == start:
        cnt = 0
        start += 1
    a,b,c = BFS(start)
    if a==-1 and b==-1 and c==-1:
        print(time)
        break
    else:
        q.append((a,b,0))
        array[a][b] = 0
        now_x = a
        now_y = b
        time += c
        cnt += 1