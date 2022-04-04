import sys
import heapq

input = sys.stdin.readline

#기본 정보
n, e = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

#함수 정의
def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
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


v1, v2 = map(int, input().split())

distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

#(시작노드 -> 정점1) + (정점1 -> 정점2) + (정점2 -> 마지막노드)
v1_path = distance[v1] + v1_distance[v2] + v2_distance[n]
#(시작노드 -> 정점2) + (정점2 -> 정점1) + (정점1 -> 마지막노드)
v2_path = distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)
print(result if result < INF else -1)
