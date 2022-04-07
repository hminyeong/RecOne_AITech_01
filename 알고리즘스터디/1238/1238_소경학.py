import heapq
n, m, x = map(int,input().split())
array = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,c = map(int,input().split())
    array[s].append([c,e])

def search(start,end):
    hp = []
    heapq.heappush(hp,[0,start])
    visit = [False for _ in range(n+1)]
    while hp:
        nlist = heapq.heappop(hp)
        cost = nlist[0]
        node = nlist[1]
        if node == end:
            return cost
        visit[node] = True
        for i in array[node]:
            if visit[i[1]] == False:
                heapq.heappush(hp,[cost+i[0],i[1]])

hpp = []
heapq.heappush(hpp,[0,x])
visited = [-1 for _ in range(n+1)]
visited[x] = 0
while hpp:
    nlist = heapq.heappop(hpp)
    cost = nlist[0]
    node = nlist[1]
    if visited[node] == -1:
        visited[node] = cost
    for i in array[node]:
        if visited[i[1]] == -1:
            heapq.heappush(hpp,[cost+i[0],i[1]])
answer = 0
for i in range(1,n+1):
    answer = max(answer,search(i,x)+visited[i])

print(answer)
