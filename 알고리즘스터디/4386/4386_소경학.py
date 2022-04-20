import heapq
import math
n = int(input())
array = []
for _ in range(n):
    a,b = map(float,input().split())
    array.append([a,b])
parent = [i for i in range(n)]
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

check = []
for i in range(n-1):
    for j in range(i+1,n):
        tt = math.sqrt((array[i][0]-array[j][0])**2 + (array[i][1]-array[j][1])**2)
        heapq.heappush(check,[tt,i,j])
line = 0
answer = 0
while True:
    if line == n-1:
        break
    tt,x,y = heapq.heappop(check)
    xx = find(x)
    yy = find(y)
    
    if xx != yy:
        union(xx,yy)
        answer += tt
        line += 1
print(answer)

