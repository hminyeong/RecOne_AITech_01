import sys
import heapq

input = sys.stdin.readline

#기본 정보
n,m,x = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

#함수 정의
def dijkstra(x):
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q,(0,x))
    distance[x] = 0
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

#출력
result = 0
for i in range(1,n+1):
    go = dijkstra(i) #각 학생들의 다른 마을까지 최단거리 리스트
    back = dijkstra(x) #파티하는 마을에서 각 학생들의 집까지의 최단거리 리스트
    result = max(result, go[x] + back[i]) #(학생마을~파티마을) + (파티마을~학생마을)
print(result)
