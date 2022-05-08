R, C, M = map(int,input().split())
array = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(M):
    a,b,c,d,e = map(int,input().split())
    array[a-1][b-1]=[c,d-1,e]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def solve():
    temp = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if array[i][j] != 0:
                s,d,z = array[i][j][0],array[i][j][1],array[i][j][2]
                ns = s
                x = i
                y = j
                while ns>0:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0<=nx<R and 0<=ny<C:
                        ns -= 1
                        x = nx
                        y = ny
                    else:
                        if d==0:d=1
                        elif d==1:d=0
                        elif d==2:d=3
                        elif d==3:d=2
                if temp[x][y] == 0:
                    temp[x][y] = [s,d,z]
                else:
                    if temp[x][y][2] < z:
                        temp[x][y] = [s,d,z]
    return temp
cnt = 0
for i in range(C):
    for j in range(R):
        if array[j][i] != 0:
            cnt += array[j][i][2]
            array[j][i] = 0
            break
    array = solve()

print(cnt)