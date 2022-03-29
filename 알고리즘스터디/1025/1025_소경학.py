import math
import sys
input = sys.stdin.readline
total = set()
def DFS(x,y,dx,dy,s):
    total.add(s)
    nx = x + dx
    ny = y + dy
    if 0<=nx<n and 0<=ny<m:
        DFS(nx,ny,dx,dy,s+array[nx][ny])
    return
def check(num):
    temp = int(math.sqrt(num))
    if temp**2 == num:
        return True
    return False
array = []
n, m = map(int,input().split())
for _ in range(n):
    array.append(list(input()))

for i in range(n):
    for j in range(m):
        for k in range(n):
            for l in range(m):
                if [i,j] == [k,l]:
                    total.add(array[i][j])
                else:
                    DFS(k,l,k-i,l-j,array[i][j]+array[k][l])

answer = -1
for i in total:
    if check(int(i)):
        answer = max(answer,int(i))
print(answer)