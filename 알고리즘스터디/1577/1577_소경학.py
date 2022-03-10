import sys
input = sys.stdin.readline

n, m = map(int,input().split())
n += 1
m += 1
t = int(input())
no_way = [[0 for _ in range(m+1)] for _ in range(n+1)]
for _ in range(t):
    a,b,c,d = map(int,input().split())
    array = [[a,b],[c,d]]
    array.sort()
    if array[0][0] != array[1][0]:
        # 북 1 서 2 둘 다 3
        if no_way[array[1][0]][array[1][1]] == 0:
            no_way[array[1][0]][array[1][1]] = 1
        elif no_way[array[1][0]][array[1][1]] == 2:
            no_way[array[1][0]][array[1][1]] = 3
    elif array[0][1] != array[1][1]:
        if no_way[array[1][0]][array[1][1]] == 0:
            no_way[array[1][0]][array[1][1]] = 2
        elif no_way[array[1][0]][array[1][1]] == 1:
            no_way[array[1][0]][array[1][1]] = 3
    
way = [[0 for _ in range(m)] for _ in range(n)]
way[0][0] = 1
for i in range(1,m):
    if way[0][i-1] == 0:
        way[0][i] = 0
    else:
        if no_way[0][i] == 2:
            way[0][i] = 0
        else:
            way[0][i] = 1
for i in range(1,n):
    if way[i-1][0] == 0:
        way[i][0] = 0
    else:
        if no_way[i][0] == 1:
            way[i][0] = 0
        else:
            way[i][0] = 1

for i in range(1,n):
    for j in range(1,m):
        if no_way[i][j] == 0:
            way[i][j] += (way[i][j-1]+way[i-1][j])
        elif no_way[i][j] == 1:
            way[i][j] += way[i][j-1]
        elif no_way[i][j] == 2:
            way[i][j] += way[i-1][j]

print(way[n-1][m-1])
