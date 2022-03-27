import sys
import heapq

input = sys.stdin.readline

#기본 정보
V, E = map(int, input().split()) #정점 개수, 간선 개수
k = int(input()) #시작 정점의 번호
INF = int(1e9)
distance = [INF] * (V+1)
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w)) # u -> v로 가는 간선w 존재


#함수 정의
def dijkstra(k):
    q = []
    heapq.heappush(q, (0,k))
    distance[k] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(k)

#출력
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])