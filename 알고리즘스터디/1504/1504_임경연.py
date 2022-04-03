import sys
import heapq

input = sys.stdin.readline

N, E = map(int, input().split())

space = [[] for _ in range(N)]

for i in range(E):
    a, b, c = map(int, input().split())
    space[a-1].append((b-1, c))
    space[b-1].append((a-1, c))

A, B = map(int, input().split())

INF = int(1e20)


def dijkstra(start):
    distance = [INF for _ in range(N)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue
        
        for next in space[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

    return distance

a = dijkstra(0)
b = dijkstra(A-1)
c = dijkstra(B-1)

if a[N-1] == INF:
    print(-1)
else:
    print(min(a[A-1]+b[B-1]+c[N-1], a[B-1]+b[N-1]+c[A-1]))

