import sys
import heapq


input = sys.stdin.readline

V, E = map(int, input().split())

x = int(input())

INF = int(1e9)

graph = [[] for _ in range(V)]

distance = [INF] * V

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue
        
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(x-1)

for i in range(len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])



