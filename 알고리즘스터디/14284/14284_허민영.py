import sys
import heapq

input = sys.stdin.readline

#기본 정보
n,m = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

s,t = map(int, input().split())
#함수 정의
def dijkstra(s):
    q = []
    heapq.heappush(q,(0,s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
    return distance

dijkstra(s)
print(distance[t])
