import heapq
import sys
input = sys.stdin.readline
n, e = map(int,input().split())
array = [[] for _ in range(n+1)]
for _ in range(e):
    start,end,cost = map(int,input().split())
    array[start].append([end,cost])
    array[end].append([start,cost])
v,w = map(int,input().split())
q = []
heapq.heappush(q,[0,1])
line1 = 0 # 1 2
line2 = 0 # 1 3
line3 = 0 # 2 3
line4 = 0 # 3 2
line5 = 0 # 2 4
line6 = 0 # 3 4
line7 = 0
visit = [False for _ in range(n+1)]
visit[1] = True
while q:
    cst, node = heapq.heappop(q)
    if node == v:
        line1 = cst
        break
    for i in array[node]:
        if visit[i[0]] == False:
            visit[i[0]] = True
            heapq.heappush(q,[cst+i[1],i[0]])

q = []
heapq.heappush(q,[0,1])
visit = [False for _ in range(n+1)]
visit[1] = True
while q:
    cst, node = heapq.heappop(q)
    if node == w:
        line2 = cst
        break
    for i in array[node]:
        if visit[i[0]] == False:
            visit[i[0]] = True
            heapq.heappush(q,[cst+i[1],i[0]])

q = []
heapq.heappush(q,[0,v])
visit = [False for _ in range(n+1)]
visit[v] = True
while q:
    cst, node = heapq.heappop(q)
    if node == w:
        line3 = cst
        break
    for i in array[node]:
        if visit[i[0]] == False:
            visit[i[0]] = True
            heapq.heappush(q,[cst+i[1],i[0]])

q = []
heapq.heappush(q,[0,w])
visit = [False for _ in range(n+1)]
visit[w] = True
while q:
    cst, node = heapq.heappop(q)
    if node == v:
        line4 = cst
        break
    for i in array[node]:
        if visit[i[0]] == False:
            visit[i[0]] = True
            heapq.heappush(q,[cst+i[1],i[0]])

q = []
heapq.heappush(q,[0,v])
visit = [False for _ in range(n+1)]
visit[v] = True
while q:
    cst, node = heapq.heappop(q)
    if node == n:
        line5 = cst
        break
    for i in array[node]:
        if visit[i[0]] == False:
            visit[i[0]] = True
            heapq.heappush(q,[cst+i[1],i[0]])

q = []
heapq.heappush(q,[0,w])
visit = [False for _ in range(n+1)]
visit[w] = True
while q:
    cst, node = heapq.heappop(q)
    if node == n:
        line6 = cst
        break
    for i in array[node]:
        if visit[i[0]] == False:
            visit[i[0]] = True
            heapq.heappush(q,[cst+i[1],i[0]])

q = []
heapq.heappush(q,[0,1])
visit = [False for _ in range(n+1)]
visit[1] = True
while q:
    cst, node = heapq.heappop(q)
    if node == n:
        line7 = cst
        break
    for i in array[node]:
        if visit[i[0]] == False:
            visit[i[0]] = True
            heapq.heappush(q,[cst+i[1],i[0]])

if line7 == 0 or (line1==0 and line2==0) or line3 == 0 or (line5==0 and line6==0): 
    print(-1)
else:
    print(min(line1+line3+line6,line2+line4+line5))